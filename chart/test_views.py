from django.test import TestCase
from django.shortcuts import get_object_or_404

class TestChartViews(TestCase):

    def test_get_charts_page(self):
        #use built in helper to fake an url request
        page = self.client.get("/chart/charts/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "graphs.html")
    def test_get_bugs_stats(self):
        #use built in helper to fake an url request
        page = self.client.get("/chart/bugs/")
        self.assertEqual(page.status_code, 200)
    def test_get_features_stats(self):
        #use built in helper to fake an url request
        page = self.client.get("/chart/features/")
        self.assertEqual(page.status_code, 200)
    def test_get_issues_data(self):
        #use built in helper to fake an url request
        page = self.client.get("/chart/chart_issues/")
        self.assertEqual(page.status_code, 200)
    def test_get_duration_data(self):
        #use built in helper to fake an url request
        page = self.client.get("/chart/time_spent/")
        self.assertEqual(page.status_code, 200)

