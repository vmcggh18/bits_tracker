from django.test import TestCase
from .forms import UserLoginForm, UserRegistrationForm
from django import forms
from django.contrib.auth.models import User

class TestTrackerUserLoginForm(TestCase):
 
    def test_can_create_an_item_with_just_a_username(self):
        #instantiate this object using a dictionary
        form = UserLoginForm({'username': 'Create Tests'})
        self.assertFalse(form.is_valid())
        
    def test_correct_message_for_missing_name(self):
        form = UserLoginForm({'username': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['username'], [u'This field is required.'])
        
    def test_registerationForm_data_is_valid(self):
        valid_data = {"email": "user@example.com", 
        "password": "secret", 
        "confirm": "secret"}
        form = UserRegistrationForm(data=valid_data)
        form.is_valid()
        self.assertTrue(form.errors)
        
    def test_passwords_must_match(self):
        invalid_data = {"email": "user@example.com", 
        "password1": "secret", 
        "password2": "anothersecret"}
        form = UserRegistrationForm(data=invalid_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password2'], ['Passwords must match']) 
  
   
   
    
   