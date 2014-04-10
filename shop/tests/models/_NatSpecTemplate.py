""" @Imports """
from cuescience_shop.tests.support.support import ClientTestSupport

from django.test.testcases import TestCase


class _NatSpecTemplate(TestCase):
    def setUp(self):
        self.client_test_support = ClientTestSupport(self)

    def test(self):
        """ @MethodBody """