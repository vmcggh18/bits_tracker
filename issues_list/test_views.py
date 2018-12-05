from django.test import TestCase
from django.test.client import Client
from django.shortcuts import get_object_or_404
from .models import Item
from .forms import ItemForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#from django.core.urlresolvers import reverse


class TestViews(TestCase):

    def test_get_issues_list_page(self):
        #use built in helper to fake an url request
        page = self.client.get("/issues_list/issues_list/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "issues_list.html")
    
    def test_create_an_item_page(self):
        page = self.client.get("/issues_list/issues_list/add")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "itemform.html")
        
   #test the edit url using the format method to pass in an id 
    def test_edit_an_item_page(self):
        #create an instance of the item model
        item = Item(name="Create a Test")
        item.save()
        page = self.client.get("/issues_list/issues_list/edit/{0}".format(item.id))
        self.assertEqual(page.status_code, 301)
  
    def test_get_edit_page_for_item_that_does_not_exist(self):
        page = self.client.get("/edit/1")
        self.assertEqual(page.status_code, 404)
        
    def test_get_comment_url(self):
        item = Item(name="Create a Test")
        item.save()
        page = self.client.get("/issues_list/issue_comment/{0}".format(item.id))
        self.assertEqual(page.status_code, 301)
        
    def test_get_issue_detail_url(self):
        item = Item(name = 'Create a test')
        item.save()
        page = self.client.get ("/issues_list/issue_detail/{0}".format(item.id))
        self.assertEqual(page.status_code, 301)
        #self.assertTemplateUsed(page, "issue_detail.html")
        
        
    # def test_create_an_item(self):
    #     response = self.client.post("/issues_list/add/", {"name": "Create a Test"})
        #item = get_object_or_404(Item, pk=1)
        # self.assertEqual(response, 'Create a test')
    # def test_post_edit_an_item(self):
    #     item = Item(name="Create a Test")
    #     item.save()
    #     id = item.id

    #     response = self.client.post("/issues_list/edit/{0}".format(id), {"name": "A different name"})
    #     item = get_object_or_404(Item, pk=id)

    #     self.assertEqual("A different name", item.name)
    # def setUp(self):
    #     self.c = Client()
    
    # def get_issues_detail(self):
    #     response = self.c.get('/issue_detail/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, "issue_detail.html")
    
        