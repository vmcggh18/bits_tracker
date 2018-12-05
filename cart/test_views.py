from django.test import TestCase, Client
from django.shortcuts import get_object_or_404
from .models import CartItem
from issues_list.models import Item


class TestViews(TestCase):

    def test_get_cart_contents_page(self):
         #use built in helper to fake an url request
        page = self.client.get("/cart/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "cart.html")
        
    def test_post_get_view_cart(self):
        c = self.client.get("/cart/") 
        self.assertEqual(c.status_code, 200)