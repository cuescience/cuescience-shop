""" @Imports """
from django.test.testcases import TestCase
from cuescience_cart.tests.support.support import TestSupport




class TestRemoveNonExistingProduct(TestCase):
    def setUp(self):
        self.test_support = TestSupport(self)

    def test(self):
        """
         The code in this method is generated from: /de.iljabauer.projects.natspec.python/cuescience_shop/tests/views/remove_view/test_remove_non_existing_product.natspec
         Never change this method or any contents of this file, all local changes will we overwritten.
        """
        