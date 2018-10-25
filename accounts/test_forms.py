from django.test import TestCase
from .forms import UserLoginForm
from django import forms

class TestTrackerUserLoginForm(TestCase):
 
    def test_can_create_an_item_with_just_a_username(self):
        #instantiate this object using a dictionary
        form = UserLoginForm({'username': 'Create Tests'})
        self.assertFalse(form.is_valid())
    def test_correct_message_for_missing_name(self):
        form = UserLoginForm({'username': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['username'], [u'This field is required.'])
   