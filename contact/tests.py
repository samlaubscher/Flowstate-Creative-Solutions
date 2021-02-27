from django.urls import reverse, resolve
from django.test import TestCase
from .views import contact


class ContactPageTests(TestCase):

    def test_contact_status_code(self):
        url = reverse('contact')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_contact_url_resolves_contact_view(self):
        view = resolve('/contact/')
        self.assertAlmostEquals(view.func, contact)
