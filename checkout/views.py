from django.shortcuts import redirect, render, reverse
from django.contrib import messages


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your cart at the moment")
        return redirect(reverse('products'))
    
    template = 'checkout/checkout.html'
    context = {}

    return render(request, template, context)
