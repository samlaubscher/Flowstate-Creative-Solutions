from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages

from products.models import Product


def view_cart(request):
    """ A view to render the cart contents page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a product to the cart """

    product = Product.objects.get(pk=item_id)
    quantity = int(1)
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        messages.info(request, f'You already have {product.name} in your cart')
    else:
        cart[item_id] = quantity
        messages.success(request, f'Added {product.name} to your cart')

    request.session['cart'] = cart
    return redirect(redirect_url)


def remove_from_cart(request, item_id):
    """Remove the item from the shopping cart"""

    try:
        cart = request.session.get('cart', {})
        cart.pop(item_id)

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
