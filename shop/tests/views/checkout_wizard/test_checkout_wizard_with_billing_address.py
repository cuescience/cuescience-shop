""" @Imports """
from django.test.testcases import TestCase
from cuescience_cart.tests.support.support import TestSupport




class TestCheckoutWizardWithBillingAddress(TestCase):
    def setUp(self):
        self.test_support = TestSupport(self)

    def test(self):
        """
         The code in this method is generated from: /cuescience-shop/shop/tests/views/checkout_wizard/test_checkout_wizard_with_billing_address.natspec
         Never change this method or any contents of this file, all local changes will we overwritten.
        """
        