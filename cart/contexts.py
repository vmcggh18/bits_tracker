from django.shortcuts import get_object_or_404
from issues_list.models import Item


def cart_contents(request):
#     """
#     Ensures that the cart contents are available when rendering every page
#     """
    cart = request.session.get('cart', {})
    
    cart_items = []
    total = 0
    item_count = 0
    for id, upvote in cart.items():
        item = get_object_or_404(Item, pk=id)
        fee = item.price * upvote
        total += upvote * item.price
        item_count += upvote
        cart_items.append({'id':id, 'upvote': upvote, 'item': item, 'fee' : fee})
    #return key value pair dict    
    return { 'cart_items': cart_items, 'total' : total, 'item_count' : item_count }
  
       
     