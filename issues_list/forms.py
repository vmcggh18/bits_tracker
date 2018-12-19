from django import forms
from .models import Item, Votefor, Comment


class ItemForm(forms.ModelForm):
    
    class Meta:
        model = Item
        fields = ('name', 'content', 'category')
        #order with respect to fee and upvotes decsending, then status
        ordering = ['fee', '-upvotes', 'status']
        
class ItemEditForm(forms.ModelForm):
    
    class Meta:
        model = Item
        fields = ('name', 'content', 'category', 'status', 'assigned_to', 'assigned_date', 'completed_date', 'progress')
        #order with respect to fee and upvotes decsending, then status
        ordering = ['fee', '-upvotes', 'status']        
        
class VoteforForm(forms.ModelForm):
    
    class Meta:
        model = Votefor
        exclude =['user']
        
class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('text', 'image')

        