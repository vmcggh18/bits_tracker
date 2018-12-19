from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    """
    A Blog Post
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True,
                                          default=timezone.now)
    views = models.IntegerField(default=0)
    tag = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to="img", blank=True, null=True)
    
    def approved_postcomments(self):
        return self.comments.filter(approved_postcomment=True)

    def __str__(self):
        return self.title
        
class PostComment(models.Model):
    """
    Comment on Blog
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name = 'comments')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    text = models.TextField(max_length=200, blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="img", blank=True, null=True)
    approved_postcomment =  models.BooleanField(default=False)
    
    def approve(self):
        self.approved_postcomment = True
        self.save()
    
    def __str__(self):
        return self.text
    class Meta:
         ordering = ['-created_date',]  