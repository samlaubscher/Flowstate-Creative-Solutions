from django.shortcuts import render, redirect


def view_cart(request):
    """ A view to render the cart contents page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a product to the cart """

    quantity = int(1)
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] = quantity # add error message here instead?
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)
