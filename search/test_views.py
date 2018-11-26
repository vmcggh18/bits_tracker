from django.test import TestCase

class TestSearchViews(TestCase):
    
    def test_do_search(self):
        page = self.client.get("/issues_list/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "issues_list.html")
    def test_search_initiated(self):
        page = self.client.get("/search/?q=")
        self.assertEqual(page.status_code, 200)