from django.urls import reverse, resolve
from django.test import TestCase
from .views import profile, order_history


class ProfilePageTests(TestCase):
    """ Profile page tests for non logged in users """

    def test_profile_status_code(self):
        url = reverse('profile')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)

    def test_profile_url_resolves_profile_view(self):
        view = resolve('/profile/')
        self.assertAlmostEquals(view.func, profile)

    def test_order_history_redirect_status_code(self):
        url = reverse('order_history', args=('1'))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)

    def test_order_history_url_resolves_order_history_view(self):
        view = resolve('/profile/order_history/1')
        self.assertAlmostEquals(view.func, order_history)
