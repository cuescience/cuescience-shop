from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe
from models_abstract import ProductBase, ClientBase, OrderBase, AddressBase


class Product(ProductBase):
    pass


class Client(ClientBase):
    def save(self, *args, **kwargs):
        super(Client, self).save(*args, **kwargs)
        if not self.client_number:
            self.generate_client_number()
            self.save()

    def generate_client_number(self):
        self.client_number = "{0:04d}".format(self.id)


class Order(OrderBase):
    def save(self, *args, **kwargs):
        super(Order, self).save(*args, **kwargs)
        if not self.order_number:
            self.generate_order_number()
            self.save()

    def generate_order_number(self):
        self.order_number = "{0:04d}".format(self.id)

    def view_order_link(self):
        url = reverse('admin:view_order', kwargs={'object_id': self.pk})
        return mark_safe("<a href='%s'>View</a>" % url)
    view_order_link.short_description = "View order"

class Address(AddressBase):
    pass

