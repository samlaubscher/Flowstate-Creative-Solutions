from django.urls import reverse, resolve
from django.test import TestCase
from .views import view_cart


class TestCartPage(TestCase):
    """ Tests for the cart page """

    def test_view_cart_status_code(self):
        url = reverse('view_cart')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_cart_url_resolves_view_cart_view(self):
        view = resolve('/cart/')
        self.assertAlmostEquals(view.func, view_cart)
