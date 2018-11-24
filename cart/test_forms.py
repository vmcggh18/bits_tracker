from django.test import TestCase
from .forms import CartItemForm
from django import forms

class TestTrackerCart(TestCase):
    def test_can_create_an_item_with_just_a_quantity(self):
        #instantiate this object using a dictionary
        form = CartItemForm({'quantity': 'Create Tests'})
        self.assertFalse(form.is_valid())