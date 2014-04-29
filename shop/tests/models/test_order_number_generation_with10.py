""" @Imports """
from cuescience_shop.tests.support.support import ClientTestSupport

from django.test.testcases import TestCase


class TestOrderNumberGenerationWith10(TestCase):
    def setUp(self):
        self.client_test_support = ClientTestSupport(self)

    def test(self):
        """
         The code in this method is generated from: /cuescience-shop/shop/tests/models/test_order_number_generation_with_10.natspec
         Never change this method or any contents of this file, all local changes will we overwritten.
        """
        