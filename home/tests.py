from django.test import TestCase
from django.shortcuts import get_object_or_404
from django.apps import apps
from .apps import HomeConfig

# Create your tests here.
class TestViews(TestCase):
    # test home page loads
    def test_get_home_page(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "index.html")
        # test about page loads
    def test_get_about_page(self):
        page = self.client.get("/home/about/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "about.html")
    def test_get_activities_page(self):
        page = self.client.get("/home/activities/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "activities.html")
    def test_get_docs_page(self):
        page = self.client.get("/home/documentation/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "documentation.html")
        
    # test apps.py file

    def test_app(self):
        self.assertEqual("home", HomeConfig.name)
        self.assertEqual("home", apps.get_app_config("home").name)