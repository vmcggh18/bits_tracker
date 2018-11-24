from django.apps import apps
from django.test import TestCase
from .apps import ChartConfig

class TestChartConfig(TestCase):

    def test_app(self):
        self.assertEqual("chart", ChartConfig.name)
        self.assertEqual("chart", apps.get_app_config("chart").name)
