from django.apps import apps
from django.test import TestCase
from .apps import IssuesListConfig

class TestIssuesListConfig(TestCase):

    def test_app(self):
        self.assertEqual("issues_list", IssuesListConfig.name)
        self.assertEqual("issues_list", apps.get_app_config("issues_list").name)
