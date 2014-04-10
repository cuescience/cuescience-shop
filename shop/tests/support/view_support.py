from decimal import Decimal
from django.test import TestCase
from natspec_utils.decorators import TextSyntax
from cuescience_shop.models import Product, Client, Order
from django.test.client import Client as TestClient
from cart.cart import Cart


class Request(object):
    def __init__(self):
        self.data = {}
        
class UpdateRequest(Request):
    pass

class CheckoutRequest(Request):
    pass

class TestSupport(object):
    def __init__(self, test_case):
        self.test_case = test_case
        self.client = TestClient()

    @TextSyntax("Create product #1 for #2", types=["list<str>", "float"])
    def create_product(self, title_words, price):
        title = " ".join(title_words)
        product = Product(title=title, price=price)
        product.save()

    @TextSyntax("Add #1 to cart", types=["list<str>", ], return_type="Response")
    def add_to_cart(self, title_words):
        title = " ".join(title_words)
        product = Product.objects.get(title=title)
        return self.add_product_to_cart(product.id)
    
    @TextSyntax("Add product #1 to cart", types=["int", ], return_type="Response")
    def add_product_to_cart(self, product_id):
        response = self.client.post("/cart/add/%s/" % product_id)
        return response
    
    @TextSyntax("Select cart", return_type="Cart")
    def select_cart(self):
        return Cart(self.client).cart
    
    @TextSyntax("Checkout cart", return_type="Response")
    def checkout_cart(self):
        response = self.client.get("/cart/checkout/")
        return response
    
    @TextSyntax("Enter data:", return_type="CheckoutRequest")
    def submit_data(self):
        request = CheckoutRequest()
        return request
    
    
    @TextSyntax("- current step: #1", types=["int", "CheckoutRequest"], return_type="CurrentStep")
    def current_step_data(self, step, request):
        request.data.update({"checkout_wizard-current_step": step})
        return step
        
    @TextSyntax("- #1: #2", types=["list<str>", "list<str>", "CheckoutRequest", "CurrentStep"])
    def collect_checkout_data(self, key_words, value_words, request, step):
        key = "_".join(key_words)
        value = " ".join(value_words)
        request.data.update({"%s-%s"%(step,key): value})
        
    @TextSyntax("Submit", types=["CheckoutRequest"], return_type="Response")
    def submit(self, request):
        response = self.client.post("/cart/checkout/", request.data)
        return response
    
    @TextSyntax("Remove #1 from cart", types=["list<str>", ], return_type="Response")
    def remove_from_cart(self, title_words):
        title = " ".join(title_words)
        product = Product.objects.get(title=title)
        return self.remove_product_from_cart(product.id)

    @TextSyntax("Remove product #1 from cart", types=["int", ], return_type="Response")
    def remove_product_from_cart(self, product_id):
        response = self.client.post("/cart/remove/%s/" % product_id)
        return response

    @TextSyntax("Update cart:", return_type="UpdateRequest")
    def update_cart(self):
        return UpdateRequest()

    @TextSyntax("- #1 to quantity #2", types=["list<str>", "int", "UpdateRequest" ])
    def update_to_quantity(self, title_words, quantity, update_request):
        title = " ".join(title_words)
        product = Product.objects.get(title=title)
        update_request.data.update({"quantity-%s" % product.id: quantity})
        
    @TextSyntax("Send update", types=["UpdateRequest"], return_type="Response")
    def send_update(self, update_request):
        response = self.client.post("/cart/update/", update_request.data)
        return response

    @TextSyntax("Send get to #1", types=["str", ], return_type="Response")
    def send_get_to_url(self, url):
        response = self.client.get(url)
        return response

    @TextSyntax("Assert status code: #1", types=["int", "Response"])
    def assert_status_code(self, status_code, response):
        self.test_case.assertEqual(response.status_code, status_code)
        
    @TextSyntax("Assert step #1 of wizard is displayed", types=["int", "Response"])
    def assert_step_of_wizard(self, step_number, response):
        wizard = response.context['wizard']
        current_step = wizard['steps'].current
        self.test_case.assertEqual(current_step, '%s'%step_number, msg="Current step should be step %s, but was %s!"%(step_number, current_step))
        

    @TextSyntax("Assert total cart item count: #1", types=["int", "Response"])
    def assert_total_item_count(self, total_count, response):
        cart = Cart(self.client)
        count = cart.count()
        self.test_case.assertEqual(total_count, count)

    @TextSyntax("Assert total cart price: #1", types=["float", "Response"])
    def assert_total_cart_price(self, total_price, response):
        cart = Cart(self.client)
        price = cart.summary()
        self.test_case.assertEqual(total_price, price)

    @TextSyntax("Assert #1 #2 in cart for #3", types=["int", "list<str>", "float", "Response"])
    def assert_specific_item_in_cart(self, total_count, title_words, price, response):
        title = " ".join(title_words)
        product = Product.objects.get(title=title)
        cart = Cart(self.client)
        for item in cart:
            if product == item.product:
                self.test_case.assertEqual(total_count, item.quantity)
                self.test_case.assertEqual(price, item.total_price)
                return
        self.test_case.assertFalse(True, msg="Product not found: %s" % product.title)
        
    @TextSyntax("Assert #1 is not in cart", types=["list<str>", "Response"])
    def assert_specific_item_not_in_cart(self, title_words, response):
        title = " ".join(title_words)
        product = Product.objects.get(title=title)
        cart = Cart(self.client)
        for item in cart:
            self.test_case.assertFalse(product == item.product, msg="The %s product should not be in cart!" % title)
            
    @TextSyntax("Select client: #1, #2", types=["list<str>","list<str>"], return_type="Client")
    def select_client(self, first_name_words, last_name_words):
        first_name = " ".join(first_name_words)
        last_name = " ".join(last_name_words)
        client = Client.objects.get(first_name=first_name, last_name=last_name)
        return client
    
    @TextSyntax("Assert client has #5 address: #1, #2, #3, #4", types=["list<str>", "list<str>", "str", "list<str>", "str", "Client"])
    def assert_client_shipping_address(self, street_words, number_words, postcode, city_words, address_type, client):
        street = " ".join(street_words)
        number = " ".join(number_words)
        city = " ".join(city_words)
        
        address = getattr(client,"%s_address"%address_type)
        self.test_case.assertEqual(street, address.street)
        self.test_case.assertEqual(number, address.number)
        self.test_case.assertEqual(postcode, address.postcode)
        self.test_case.assertEqual(city, address.city)
        
    @TextSyntax("Assert order with cart exists", types=["Cart"], return_type="Order")
    def assert_order_with_cart_exists(self, cart):
        order = Order.objects.get(cart=cart)
        return order
    
    @TextSyntax("Assert order has abovementioned client", types=["Order", "Client"])
    def assert_order_has_client(self, order, client):
        self.test_case.assertEqual(client, order.client)
        
        
        
        
        
        
