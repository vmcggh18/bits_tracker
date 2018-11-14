from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone
from datetime import datetime
from vote.models import VoteModel

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=30, blank=False)
    content = models.TextField(max_length=200, blank=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    Category = (
        ('Feature', 'Feature'),
        ('Bug', 'Bug'),
    )
    category = models.CharField(max_length=20, choices=Category, blank=False, default = False)
    created_date = models.DateTimeField(auto_now_add=True)
    upvotes = models.IntegerField(default=0)
    Status = (
        ('Pending', 'Pending'),
        ('Ongoing', 'Ongoing'),
        ('Completed', 'Completed'),
    )
    status = models.CharField(max_length=20, choices=Status, blank=False, default = False) 
    Assigned_to = (
        ('Not yet assigned', 'Not yet assigned'),
        ('Admin1', 'Admin1'),
        ('The Prof', 'The Prof'),
        ('Jane Doe', 'Jane Doe'),
        ('Jane Smith', 'Jane Smith'),
        ('John Doe', 'John Doe'),
        ('John Smith', 'John Smith'),
    )
    assigned_to = models.CharField(max_length=30, choices=Assigned_to, blank=False, default="Not yet Assigned")
    completed_date = models.DateTimeField(null=True, blank=True, auto_now=True)
    progress = models.TextField(max_length=200, default='', help_text="Add progress comments to the status")
    fee = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    price= models.DecimalField(max_digits=6, decimal_places=2, default=50)
   # define names in admin panel
    def __str__(self):
        return self.name
    # sort the data by upvotes decsending
    class Meta:
        ordering = ['-upvotes']
        
class Votefor(models.Model):
    user = models.ForeignKey(User, related_name ='user_votes')
    item = models.ForeignKey(Item, related_name="item_votes")
    voteup = models.BooleanField(default=False)
    
    class Meta:
        unique_together = ('user', 'item')

   
class Comment(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name = 'comments')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    text = models.TextField(max_length=200, blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    approved_comment =  models.BooleanField(default=False)
    
    def approve(self):
        self.approved_comment = True
        self.save()
    
    def __str__(self):
        return self.text
          



