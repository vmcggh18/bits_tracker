from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from django.conf import settings
from django.utils import timezone
from issues_list.models import Item
import stripe
# Create your views here.

# import stripe key
stripe.api_key = settings.STRIPE_SECRET

@login_required()
def checkout(request):
    """ Get forms to be filled out """
    if request.method=="POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)
        
        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()
            
            cart = request.session.get('cart', {})
            total = 0
            for id, upvote in cart.items():
                item = get_object_or_404(Item, pk=id)
                fee = item.price * upvote
                total += upvote * item.price
                order_line_item = OrderLineItem(
                    order = order,
                    item = item,
                    upvote = upvote
                    )
                order_line_item.save()
            try:
                customer = stripe.Charge.create(amount = int(total * 100),
                currency = "EUR",
                description = request.user.email,
                card = payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")
            if customer.paid:
                messages.error(request, "You have successfully paid and upvotes added to the feature")
                request.session['cart'] = {}
                for id, upvote in cart.items():
                    item = get_object_or_404(Item, pk=id)
                    item.upvotes += upvote
                    item.save()
                    item.fee += fee
                    item.save()
                return redirect(reverse('issues_list'))
            else:
                messages.error(request, "Unable to take payment")
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take a payment with that card!")
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()
    return render(request, "checkout.html", {'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE})