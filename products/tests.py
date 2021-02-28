from django.urls import reverse, resolve
from django.test import TestCase
from .views import (
    all_products,
    product_detail,
    add_product,
    edit_product,
    delete_product
)


class ProductPageTests(TestCase):

    def test_all_products_status_code(self):
        url = reverse('products')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_products_url_resolves_all_products_view(self):
        view = resolve('/products/')
        self.assertAlmostEquals(view.func, all_products)

    def test_product_detail_url_resolves_product_detail_view(self):
        view = resolve('/products/1/')
        self.assertAlmostEquals(view.func, product_detail)

    def test_add_product_redirect_status_code(self):
        url = reverse('add_product')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)

    def test_add_product_url_resolves_add_product_view(self):
        view = resolve('/products/add/')
        self.assertAlmostEquals(view.func, add_product)

    def test_edit_product_redirect_status_code(self):
        url = reverse('edit_product', args=("1"))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)

    def test_edit_product_url_resolves_edit_product_view(self):
        view = resolve('/products/edit/1/')
        self.assertAlmostEquals(view.func, edit_product)

    def test_delete_product_redirect_status_code(self):
        url = reverse('delete_product', args=("1"))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)

    def test_delete_product_url_resolves_delete_product_view(self):
        view = resolve('/products/delete/1/')
        self.assertAlmostEquals(view.func, delete_product)
