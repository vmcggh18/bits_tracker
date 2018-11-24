from django.shortcuts import render, redirect, reverse, get_object_or_404
from issues_list.models import Item
from issues_list.forms import ItemForm
from django.contrib import messages, auth
from django.contrib.auth.models import User
from issues_list.views import get_issues_list

# Create your views here.

def view_cart(request):
    """A view that renders the cart contents page"""
    return render(request, "cart.html")
    
def add_to_cart(request, id):
    """Add a quantity of the specified product to the cart"""
    upvote=int(request.POST.get('upvote'))
    
    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, upvote)
    
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
    
def adjust_cart(request, id):
    """Adjust the quantity of the specified product to the specified amount"""
    upvote = int(request.POST.get('upvote'))
    cart = request.session.get('cart', {})
    
    if upvote > 0:
        cart[id] = upvote
    else:
        cart.pop(id)
        
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))