from django import forms
from .models import Post, PostComment


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'image', 'tag', 'published_date')
        
class BlogCommentForm(forms.ModelForm):
    
    class Meta:
        model = PostComment
        fields = ('text',)
