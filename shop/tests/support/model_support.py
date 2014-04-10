from cuescience_shop.models import Client, Address, Order
from natspec_utils.decorators import TextSyntax
from cart.cart import Cart
from django.test.client import Client as TestClient


class ClientTestSupport(object):
    def __init__(self, test_case):
        self.test_case = test_case
        self.client = TestClient()
    
    @TextSyntax("Create address #1 #2 #3 #4", types=["str", "str", "str", "str"], return_type="Address")
    def create_address(self, street, number, postcode, city):
        address = Address(street=street, number=number, postcode=postcode, city=city)
        address.save()
        return address
        
    @TextSyntax("Create client #1 #2", types=["str", "str", "Address"], return_type="Client")
    def create_client(self, first_name, last_name, address):
        client = Client(first_name=first_name, last_name=last_name, shipping_address=address, billing_address=address)
        client.save()
        return client
    
    @TextSyntax("Create order", types=["Client"], return_type="Order")
    def create_order(self, client):
        cart = Cart(self.client)
        cart.create_cart()
        cart = cart.cart
        order = Order(client=client, cart=cart)
        order.save()
        return order
    
    @TextSyntax("Assert client number is #1", types=["str", "Client"])
    def assert_client_number(self, client_number, client):
        self.test_case.assertEqual(client_number, client.client_number)
        
    @TextSyntax("Assert order number is #1", types=["str", "Order"])
    def assert_order_number(self, order_number, order):
        self.test_case.assertEqual(order_number, order.order_number)
        
        
        
        
