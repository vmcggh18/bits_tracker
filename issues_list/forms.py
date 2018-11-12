from django import forms
from .models import Item, Votefor, Comment


class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('name', 'content', 'category',  'status', 'assigned_to', 'progress')
        #order_with_respect_to = 'upvotes decsending'
        ordering = ['-upvotes']
class VoteforForm(forms.ModelForm):
    
    class Meta:
        model = Votefor
        exclude =['user']
        
class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('text',)

        