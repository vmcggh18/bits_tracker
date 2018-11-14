from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from issues_list.models import Item

# Create your models here.
class CartItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name = 'item_price')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=50)
    
    def __str__(self):
        return self.item
          