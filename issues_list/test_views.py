from django.test import TestCase
from django.shortcuts import get_object_or_404
from .models import Item
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class TestViews(TestCase):

    def test_get_issues_list_page(self):
        #use built in helper to fake an url request
        page = self.client.get("/issues_list/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "issues_list.html")
    
    def test_create_an_item_page(self):
        page = self.client.get("/issues_list/add")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "itemform.html")
   #test the edit url using the format method to pass in an id 
    def test_edit_an_item_page(self):
        #create an instance of the item model
        item = Item(name="Create a Test")
        item.save()
        page = self.client.get("/issues_list/edit/{0}".format(item.id))
        self.assertEqual(page.status_code, 301)
        # self.assertTemplateUsed(page, "editform.html")
    # def test_edit_an_item_page(self):
    #     item = Item()
    #     response = item.get('/issues_list/edit/{0}')
    #     self.assertEqual(response.status_code, 200)
   
    def test_get_edit_page_for_item_that_does_not_exist(self):
        page = self.client.get("/edit/1")
        self.assertEqual(page.status_code, 404)
        