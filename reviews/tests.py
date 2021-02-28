from django.urls import reverse, resolve
from django.test import TestCase
from .views import add_product_review


class ReviewPageTests(TestCase):
    """ Review app tests for non logged in users """

    def test_add_review_status_code(self):
        url = reverse('add_product_review', args=("1"))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)

    def test_home_url_resolves_index_view(self):
        view = resolve('/products/1/add_product_review/')
        self.assertAlmostEquals(view.func, add_product_review)
