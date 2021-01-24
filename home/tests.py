from django.urls import reverse, resolve
from django.test import TestCase
from .views import index


class HomePageTests(TestCase):

    def test_home_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_home_url_resolves_index_view(self):
        view = resolve('/')
        self.assertAlmostEquals(view.func, index)
