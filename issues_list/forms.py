from django import forms
from .models import Item, Votefor, Comment


class ItemForm(forms.ModelForm):
    
    class Meta:
        model = Item
        fields = ('name', 'content', 'category')
        #order with respect to fee and upvotes decsending, then status
        ordering = ['fee', '-upvotes', 'status']
        
class ItemEditForm(forms.ModelForm):
    assigned_date =  forms.DateTimeField(input_formats=['%Y-%m-%d %H:%M:%S',], help_text="Enter as Y-m-d H:M (example 2018-11-10 11:30:00)")
    completed_date =  forms.DateTimeField(input_formats=['%Y-%m-%d %H:%M:%S',], help_text="Enter as Y-m-d H:M (example 2018-11-10 11:30:00)")
    
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
        fields = ('text',)

        