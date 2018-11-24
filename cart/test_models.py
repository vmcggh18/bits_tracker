from django.test import TestCase
from .models import CartItem

class TestCartItemModel(TestCase):
    
    def test_integer_representation(self):
        cartitem = CartItem(quantity =  0)
        self.assertEqual(int(0), cartitem.quantity)  
        
    def test_decimal_representation(self):
        cartitem = CartItem(price =  50.00)
        self.assertEqual(float(50.00), cartitem.price)  
    
    