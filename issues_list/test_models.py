from django.test import TestCase
from .models import Item, Comment, Votefor


class TestItemModel(TestCase):

    def test_content_defaults_to_False(self):
        item = Item(name="Create a Test")
        item.save()
        self.assertEqual(item.name, "Create a Test")
        self.assertFalse(item.content)
    
    def test_can_create_an_item_with_a_name_and_status(self):
        item = Item(name="Create a Test", status=True)
        item.save()
        self.assertEqual(item.name, "Create a Test")
        self.assertTrue(item.status)
        #test for the string representation of the object
    def test_item_as_a_string(self):
        # test that the instance is same name as the name that we gave the object i.e item = item
        item = Item(name="Create a Test")
        self.assertEqual("Create a Test", str(item))
        
    def test_str(self):
        test_name = Item(name='An Issue')
        self. assertEqual(str(test_name), 'An Issue')
