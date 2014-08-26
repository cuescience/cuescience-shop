""" GENERATED FILE. ALL CHANGES WILL BE OVERWRITTEN! """
from cart.models import Item
from django.conf.urls import url, patterns
from django.contrib import admin
from django.db.models import get_models, get_app
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.text import wrap
from .models import Product, Order, Client, Address


class ProductAdmin(admin.ModelAdmin):
    pass


admin.site.register(Product, ProductAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'client', "payment", "view_order_link")
    list_filter = ('client', )

    def get_urls(self):
        urls = super(OrderAdmin, self).get_urls()
        my_urls = [url(r'^(?P<object_id>\d+)/view/$', self.admin_site.admin_view(self.view_order), name='view_order'), ]
        return my_urls + urls

    def view_order(self, request, object_id):
        order = Order.objects.get(pk=object_id)
        items = Item.objects.filter(cart=order.cart)

        return render_to_response('cuescience_shop/view_order.html', RequestContext(request, {
            "order": order,
            "items": items,
        }))


admin.site.register(Order, OrderAdmin)


class ClientAdmin(admin.ModelAdmin):
    list_display = ('client_number', 'first_name', 'last_name', )
    list_filter = ('shipping_address__city', )


admin.site.register(Client, ClientAdmin)


class AddressAdmin(admin.ModelAdmin):
    pass


admin.site.register(Address, AddressAdmin)

for model in get_models(get_app('cart')):
    try:
        admin.site.register(model)
    except Exception as e:
        print "This Model is already registered: %s" % model