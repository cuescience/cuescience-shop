""" @Imports """
from django.test.testcases import TestCase
from cuescience_cart.tests.support.support import TestSupport




class TestUpdateQuantityZero(TestCase):
    def setUp(self):
        self.test_support = TestSupport(self)

    def test(self):
        """
         The code in this method is generated from: /cuescience-shop/shop/tests/views/update_view/test_update_quantity_zero.natspec
         Never change this method or any contents of this file, all local changes will we overwritten.
        """
        