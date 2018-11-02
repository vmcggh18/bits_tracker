from django import forms
from .models import Item


class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('name', 'content', 'submitted_by', 'category', 'upvotes', 'status', 'assigned_to', 'progress')
        #order_with_respect_to = 'upvotes decsending'
        ordering = ['-upvotes']
        