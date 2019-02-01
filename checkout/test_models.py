from django.test import TestCase
from .models import Order, OrderLineItem

class TestOrderModel(TestCase):

    
  def test_str(self):
        test_full_name = Order(id="id", date="date", full_name='An Issue')
        self. assertEqual(str(test_full_name), 'id-date-An Issue')
 