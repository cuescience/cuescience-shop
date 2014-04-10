""" GENERATED FILE. ALL CHANGES WILL BE OVERWRITTEN! """
from django.contrib import admin
from .models import Product,Order,Client,Address

class ProductAdmin(admin.ModelAdmin):
    pass

admin.site.register(Product, ProductAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'client', "payment")
    list_filter = ('client', )
    

admin.site.register(Order, OrderAdmin)

class ClientAdmin(admin.ModelAdmin):
    list_display = ('client_number', 'first_name', 'last_name', )
    list_filter = ('shipping_address__city', )
    

admin.site.register(Client, ClientAdmin)

class AddressAdmin(admin.ModelAdmin):
    pass

admin.site.register(Address, AddressAdmin)
