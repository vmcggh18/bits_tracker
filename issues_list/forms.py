from django import forms
from .models import Item, Votefor, Comment


class ItemForm(forms.ModelForm):
    assigned_date =  forms.DateTimeField(input_formats=['%d-%m-%Y %H:%M',])
    class Meta:
        model = Item
        fields = ('name', 'content', 'category',  'status', 'assigned_to', 'assigned_date', 'progress')
        #order_with_respect_to = 'upvotes decsending'
        ordering = ['fee', '-upvotes', 'status']
class VoteforForm(forms.ModelForm):
    
    class Meta:
        model = Votefor
        exclude =['user']
        
class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('text',)

        