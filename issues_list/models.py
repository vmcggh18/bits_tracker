from django.db import models
from django.contrib.auth.models import User, Group, Permission
from django.utils import timezone
from datetime import datetime
#from vote.models import VoteModel
from django.contrib.auth.models import User, Group, Permission
# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=30, blank=False)
    content = models.TextField(max_length=200, blank=False)
    submitted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
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
    assigned_to = models.CharField(max_length=30, blank=False, default="Not yet Assigned")
    completed_date = models.DateTimeField(null=True, blank=True)
    comments = models.TextField(max_length=200, help_text="Add comments relevant to the status")
   # define names in admin panel
    def __str__(self):
        return self.name
    # def __unicode__(self):
    #     return self.title
    # sort the data by upvotes decsending
    class Meta:
        ordering = ['-upvotes']
        permissions = (("can_add_comments", "Set new comment"),)  



