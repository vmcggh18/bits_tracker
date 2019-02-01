from django.test import TestCase
from django.shortcuts import get_object_or_404
from issues_list.models import Item
from .forms import MakePaymentForm, OrderForm

class TestViews(TestCase):
    def test_payment_made(self):
        page = self.client.get("/issues_list/issues_list/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "issues_list.html")
    def test_get_payment_form(self):
        page=self.client.get("/checkout/")
        self.assertEqual(page.status_code, 302)
        #self.assertTemplateUsed(page, "checkout.html")
  