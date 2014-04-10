from natspec_utils.stringutils import stringToUnicode as u;


from jinja2.environment import Environment
from jinja2.loaders import PackageLoader

from django_lean_modelling import helper
from django_lean_modelling.models.support import ModelSupport
from django_lean_modelling.admin.support import AdminSupport


class Models():
    
    model_support = ModelSupport()
    admin_support = AdminSupport()
    
    def generate_models(self):
        """
         The code in this method is generated from: /de.iljabauer.projects.natspec.python/cuescience_shop/specs/models/models.natspec
         Never change this method or any contents of this file, all local changes will we overwritten.
        """
        # Every Product has:
        model_Product = self.model_support.model_name_definition([u("Product")])
        
        # - a title.
        property_title = self.model_support.string_property_definition([u("title")], model_Product)
        
        # The title of the product
        self.model_support.comment_definition(['The', 'title', 'of', 'the', 'product'], property_title)
        
        # - a price as decimal:
        property_price = self.model_support.typed_decimal_property_definition([u("price")], model_Product)
        
        # The price without tax. The maximum value is 9999,99
        self.model_support.comment_definition(['The', 'price', 'without', 'tax.', 'The', 'maximum', 'value', 'is', '9999,99'], property_price)
        
        # decimal places: 2
        self.model_support.property_decimal_places_definition(2, property_price)
        
        # max digits: 6
        self.model_support.property_max_digits_definition(6, property_price)
        
        # Configure standard admin.
        admin_ = self.admin_support.configure_admin(model_Product)
        
        # Every Order has:
        model_Order = self.model_support.model_name_definition([u("Order")])
        
        # - a order number.
        property_order_number = self.model_support.string_property_definition([u("order"), u("number")], model_Order)
        
        # - one Client.
        property_Client = self.model_support.foreign_key_property_definition(u("Client"), model_Order)
        
        # The client wich has ordered.
        self.model_support.comment_definition(['The', 'client', 'wich', 'has', 'ordered.'], property_Client)
        
        # - one cart.Cart.
        property_cart_Cart = self.model_support.foreign_key_property_definition(u("cart.Cart"), model_Order)
        
        # The cart contains the ordered products, quantities and total price
        self.model_support.comment_definition(['The', 'cart', 'contains', 'the', 'ordered', 'products,', 'quantities', 'and', 'total', 'price'], property_cart_Cart)
        
        # - one exclusive cuescience_payment.Payment called payment.
        property_cuescience_payment_Payment_payment = self.model_support.one_to_one_with_name_property_definition(u("cuescience_payment.Payment"), [u("payment")], model_Order)
        
        # Configure admin to:
        admin_0 = self.admin_support.configure_admin(model_Order)
        
        # - display: order number, client.
        property_order_number__client = self.admin_support.display_definition([u("order"), u("number,"), u("client")], admin_0)
        
        # - show filter for: client.
        property_client = self.admin_support.filter_definition([u("client")], admin_0)
        
        # Every Client has:
        model_Client = self.model_support.model_name_definition([u("Client")])
        
        # - a client number:
        property_client_number = self.model_support.string_property_definition([u("client"), u("number")], model_Client)
        
        # max length: 6
        self.model_support.property_max_length_definition(6, property_client_number)
        
        # - an email.
        property_email = self.model_support.string_property_definition([u("email")], model_Client)
        
        # - a first name.
        property_first_name = self.model_support.string_property_definition([u("first"), u("name")], model_Client)
        
        # - a last name.
        property_last_name = self.model_support.string_property_definition([u("last"), u("name")], model_Client)
        
        # - one exclusive Address called billing address.
        property_Address_billing_address = self.model_support.one_to_one_with_name_property_definition(u("Address"), [u("billing"), u("address")], model_Client)
        
        # - one exclusive Address called shipping address.
        property_Address_shipping_address = self.model_support.one_to_one_with_name_property_definition(u("Address"), [u("shipping"), u("address")], model_Client)
        
        # Configure admin to:
        admin_1 = self.admin_support.configure_admin(model_Client)
        
        # - display: client number, first name, last name.
        property_client_number__first_name__last_name = self.admin_support.display_definition([u("client"), u("number,"), u("first"), u("name,"), u("last"), u("name")], admin_1)
        
        # - show filter for: shipping address__city.
        property_shipping_address__city = self.admin_support.filter_definition([u("shipping"), u("address__city")], admin_1)
        
        # Every Address (plural Addresses) has:
        model_Address_Addresses = self.model_support.model_name_with_plural_definition([u("Address")], [u("Addresses")])
        
        # - a street.
        property_street = self.model_support.string_property_definition([u("street")], model_Address_Addresses)
        
        # - a number:
        property_number = self.model_support.string_property_definition([u("number")], model_Address_Addresses)
        
        # The street number contains the number itself as well as extra characters, e.g. 41c
        self.model_support.comment_definition(['The', 'street', 'number', 'contains', 'the', 'number', 'itself', 'as', 'well', 'as', 'extra', 'characters,', 'e.g.', '41c'], property_number)
        
        # max length: 5
        self.model_support.property_max_length_definition(5, property_number)
        
        # - a postcode:
        property_postcode = self.model_support.string_property_definition([u("postcode")], model_Address_Addresses)
        
        # The German postcode, maybe not suitable for other countries.
        self.model_support.comment_definition(['The', 'German', 'postcode,', 'maybe', 'not', 'suitable', 'for', 'other', 'countries.'], property_postcode)
        
        # max length: 5
        self.model_support.property_max_length_definition(5, property_postcode)
        
        # - a city.
        property_city = self.model_support.string_property_definition([u("city")], model_Address_Addresses)
        
        # Configure standard admin.
        admin_2 = self.admin_support.configure_admin(model_Address_Addresses)
        
        
        

if __name__ == '__main__':
    model = Models()
    model.generate_models()

    env = Environment(loader=PackageLoader('cuescience_shop.specs', 'templates'), trim_blocks=False)
    template = env.get_template("model_template.py")
    
    content = template.render(models=model.model_support.models)
    
    template_admin = env.get_template("admin_template.py")
    content_admin = template_admin.render(admins=model.admin_support.admins)
    
    print model.admin_support.admins
    
    f = open("../../%s_abstract.py" % helper.convert(model.__class__.__name__), 'w')
    f.write(content)
    f.close()
    f1 = open("../../admin.py", 'w')
    f1.write(content_admin)
    f1.close()