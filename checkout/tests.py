from django.urls import reverse, resolve
from django.test import TestCase
from .views import checkout, checkout_success


class CheckoutPageTests(TestCase):

    def test_checkout_redirect_status_code(self):
        url = reverse('checkout')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)

    def test_checkout_url_resolves_checkout_view(self):
        view = resolve('/checkout/')
        self.assertAlmostEquals(view.func, checkout)

    def test_checkout_success_url_resolves_checkout_success_view(self):
        view = resolve('/checkout/checkout_success/123ordernumber')
        self.assertAlmostEquals(view.func, checkout_success)
