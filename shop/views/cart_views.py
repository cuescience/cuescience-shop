import logging
from cart import Cart
from django.conf import settings
from django.contrib.sites.models import get_current_site
from django.utils import translation
from mailtemplates.models import EMailTemplate
from payment.models import PrePayment
from payment.services.paypal import paypal
from shop.checkout_wizard import condition_step_3, CheckoutWizardBase
from shop.models import Product, Order
from django.http import Http404, HttpResponseNotAllowed
from django.shortcuts import redirect, render_to_response, render
from django.template import RequestContext
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_exempt

logger = logging.getLogger(__name__)

@never_cache
def index_view(request):
    return render_to_response("cuescience_shop/cart/index.html", RequestContext(request))

@never_cache
def add_view(request, product_id):
    if request.method != "GET":
        return HttpResponseNotAllowed(["GET"])

    next = request.GET.get("next", "/")

    cart = Cart(request)
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        raise Http404

    cart.add(product, product.price)

    return redirect(next)

@never_cache
def remove_view(request, product_id):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])

    next = request.GET.get("next", "/")

    cart = Cart(request)
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        raise Http404

    cart.remove(product)

    return redirect(next)

@never_cache
def update_view(request):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])

    next = request.GET.get("next", "/")

    cart = Cart(request)
    for item in cart:
        quantity = request.POST.get("quantity-{0}".format(item.product.pk), None)
        isNone = quantity is None

        if isNone:
            continue
        isSame = int(quantity) == item.quantity
        if isSame:
            continue

        quantity = int(quantity)
        if quantity == 0:
            item.delete()
            continue

        item.quantity = quantity
        item.save()

    return redirect(next)


class CheckoutWizard(CheckoutWizardBase):
    template_name = "cuescience_shop/cart/wizard.html"

    def create_paypalpayment(self, cart):
        paypalservice = paypal.PayPalService()

        transaction = paypal.Transaction(total=cart.summary())
        for cart_item in cart:
            print("ITEM {0}".format(cart_item))
            product = cart_item.product
            item = paypal.Item(product.title, cart_item.get_unit_price(), cart_item.quantity, "EUR", sku=product.id)
            transaction.item_list.append(item)
        #TODO add translation
        item = paypal.Item("Versand / Shipping", cart.shipping_costs(), 1, "EUR", sku=0)
        transaction.item_list.append(item)

        domain = get_current_site(self.request)
        payment_result = paypalservice.create_payment(transaction, domain)
        return payment_result

    def done(self, form_list, **kwargs):
        cart = Cart(self.request)
        cart.create_cart()
        order = Order(cart=cart.cart)

        client = form_list[0].save(commit=False)
        address = form_list[1].save()
        client.shipping_address = address
        billing_address = address
        if condition_step_3(self):
            billing_address = form_list[2].save()
        client.billing_address = billing_address
        client.save()

        order.client = client

        payment_option = self.get_cleaned_data_for_step("4").get("payment_options", None)
        print ("PAYMENT {0}".format(self.get_cleaned_data_for_step("4")))
        language = translation.get_language().upper()
        if payment_option == "PayPal":
            result = self.create_paypalpayment(cart)
            order.payment = result.paypal_payment_db
            order.save()
            # we need to do the checkout after saving the order,
            # if something went wrong
            cart.check_out()

            mail_result = EMailTemplate.objects.send("{0}_ORDER_SUCCESS_PAYPAL".format(language), client.email,
                                                     {"order": order, "billing_address": billing_address,
                                                      "shipping_address": address,
                                                      "paypal_url": order.payment.approval_url})

            if result.payment.error:
                logger.error("PayPal payment went wrong! Errors: {0}".format(result.payment.error))
                return render(self.request, "cuescience_shop/failure_paypal.html", {"order": order})
            elif not result.payment.errors and order.payment.approval_url:
                return render(self.request, "cuescience_shop/success_paypal.html", {"order": order})

        elif payment_option == "Prepayment":
            payment = PrePayment()
            payment.save()
            order.payment = payment
            order.save()
            cart.check_out()
            mail_result = EMailTemplate.objects.send("{0}_ORDER_SUCCESS_PREPAYMENT".format(language), client.email,
                                                     {"order": order, "billing_address": billing_address,
                                                      "shipping_address": address})
            return render(self.request, "cuescience_shop/success.html", {"order": order})

        return render_to_response("cuescience_shop/cart/index.html", RequestContext(self.request))
