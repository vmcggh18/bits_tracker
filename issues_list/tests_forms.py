from django.test import TestCase
from .forms import ItemForm
from django import forms

class TestTrackerIssueList(TestCase):
 
    def test_can_create_an_item_with_just_a_name(self):
        #instantiate this object using a dictionary
        form = ItemForm({'name': 'Create Tests'})
        self.assertFalse(form.is_valid())
    def test_correct_message_for_missing_name(self):
        form = ItemForm({'username': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['name'], [u'This field is required.'])

