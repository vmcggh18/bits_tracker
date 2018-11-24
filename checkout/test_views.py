from django.test import TestCase
from django.shortcuts import get_object_or_404
from issues_list.models import Item
from .forms import MakePaymentForm, OrderForm

class TestViews(TestCase):
    def test_payment_made(self):
        page = self.client.get("/issues_list/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "issues_list.html")
  