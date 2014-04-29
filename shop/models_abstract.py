""" GENERATED FILE. ALL CHANGES WILL BE OVERWRITTEN! """
from django.db import models
from django.utils.translation import ugettext as _


class ProductBase(models.Model):
    """
    :param title: The title of the product
    :param price: The price without tax. The maximum value is 9999,99
    """
    class Meta:
        abstract = True
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
    title = models.CharField(max_length=128, )
    price = models.DecimalField(max_digits=6, decimal_places=2, )
     
	
    def __unicode__(self):
        return u"%s"%self.title

class OrderBase(models.Model):
    """
    :param order_number
    :param client: The client wich has ordered.
    :param cart: The cart contains the ordered products, quantities and total price
    :param payment
    """
    class Meta:
        abstract = True
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")
    order_number = models.CharField(max_length=128, )
    client = models.ForeignKey('Client', related_name='client', )
    cart = models.ForeignKey('cart.Cart', related_name='cart', )
    payment = models.OneToOneField('payment.Payment', related_name='payment_of', )
     
	
    def __unicode__(self):
        return u"%s"%self.order_number

class ClientBase(models.Model):
    """
    :param client_number
    :param email
    :param first_name
    :param last_name
    :param billing_address
    :param shipping_address
    """
    class Meta:
        abstract = True
        verbose_name = _("Client")
        verbose_name_plural = _("Clients")
    client_number = models.CharField(max_length=6, )
    email = models.EmailField()
    first_name = models.CharField(max_length=128, )
    last_name = models.CharField(max_length=128, )
    billing_address = models.OneToOneField('Address', related_name='billing_address_of', )
    shipping_address = models.OneToOneField('Address', related_name='shipping_address_of', )
     
	
    def __unicode__(self):
        return u"%s"%self.client_number

class AddressBase(models.Model):
    """
    :param street
    :param number: The street number contains the number itself as well as extra characters, e.g. 41c
    :param postcode: The German postcode, maybe not suitable for other countries.
    :param city
    """
    class Meta:
        abstract = True
        verbose_name = _("Address")
        verbose_name_plural = _("Addresses")
    street = models.CharField(max_length=128, )
    number = models.CharField(max_length=5, )
    postcode = models.CharField(max_length=5, )
    city = models.CharField(max_length=128, )
     
	
    def __unicode__(self):
        return u"%s"%self.street
