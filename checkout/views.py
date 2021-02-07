from django.shortcuts import redirect, render, reverse
from django.contrib import messages


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your cart at the moment")
        return redirect(reverse('products'))
    
    template = 'checkout/checkout.html'
    context = {
        'stripe_public_key': 'pk_test_51I8qG6LaOwFXT33QWluNoimDTUapwNgy3udGh4YB2UNK9yI7ruffaWY7m9kSSOZCzVaVPiwyzpjZCfWplD4FsnJv00oO7PvxVu',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
