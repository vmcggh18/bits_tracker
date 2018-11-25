from django import forms
from .models import Item, Votefor, Comment


class ItemForm(forms.ModelForm):
    
    class Meta:
        model = Item
        fields = ('name', 'content', 'category')
        #order with respect to fee and upvotes decsending, then status
        ordering = ['fee', '-upvotes', 'status']
        
class ItemEditForm(forms.ModelForm):
    assigned_date =  forms.DateTimeField(input_formats=['%d-%m-%Y %H:%M',], help_text="Enter as d-m-Y H:M (example 10-11-2018 11:30) (secs not required)")
    completed_date =  forms.DateTimeField(input_formats=['%d-%m-%Y %H:%M',], help_text="Enter as d-m-Y H:M (example 10-11-2018 11:30) (secs not required)")
    
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

        