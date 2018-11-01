from django import forms
from .models import Item


class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('name', 'content', 'submitted_by', 'category', 'upvotes', 'status', 'assigned_to', 'completed_date', 'comments')
        ordering = ['-upvotes']
        #order_with_respect_to = 'upvotes'