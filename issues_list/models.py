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
    status = models.CharField(max_length=20, choices=Status, blank=False, default = "Pending") 
    Assigned_to = (
        ('Not yet', 'Not yet'),
        ('Admin1', 'Admin1'),
        ('Admin2', 'Admin2'),
        ('The Prof', 'The Prof'),
        ('Jane Doe', 'Jane Doe'),
        ('Jane Smith', 'Jane Smith'),
        ('John Doe', 'John Doe'),
        ('John Smith', 'John Smith'),
    )
    assigned_to = models.CharField(max_length=30, choices=Assigned_to, blank=False, default="Not yet")
    assigned_date = models.DateTimeField(null=True, blank=True, default=timezone.now, help_text="Enter as Y-m-d H:M:S (example 2018-11-10 11:30:00)")
    completed_date = models.DateTimeField(null=True, blank=True, default=timezone.now, help_text="Enter as Y-m-d H:M:S (example 2018-11-10 11:30:00)")
    progress = models.TextField(max_length=200, default='Queued', help_text="Add progress note relative to the status (eg In Development)")
    fee = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    price= models.DecimalField(max_digits=6, decimal_places=2, default=50)
    
    def approved_comments(self):
        return self.comments.filter(approved_comment=True)
   # define names in admin panel
    def __str__(self):
        return self.name
    # sort the data in the order shown all descending
    class Meta:
        ordering = ['-fee', '-upvotes', '-status']
        
class Votefor(models.Model):
    user = models.ForeignKey(User, related_name ='user_votes')
    item = models.ForeignKey(Item, related_name="item_votes")
    #voteup = models.BooleanField(default=False)
    
    class Meta:
        unique_together = ('user', 'item')

   
class Comment(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name = 'comments')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    text = models.TextField(max_length=200, blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="img", blank=True, null=True)
    approved_comment =  models.BooleanField(default=False)
    
    def approve(self):
        self.approved_comment = True
        self.save()
    
    def __str__(self):
        return self.text
    class Meta:
         ordering = ['-created_date',]  
          



