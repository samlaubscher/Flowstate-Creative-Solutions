from django.shortcuts import get_object_or_404, render, redirect, HttpResponse
from django.contrib import messages
from django.conf import settings

from products.models import Product


def view_cart(request):
    """
    A view to render the cart contents page with discount logic
    """

    #### DISCOUNT SECTION - POTENTIALLY REMOVE
    discount = False
    if request.GET:
        if 'dc' in request.GET:
            code = request.GET['dc'].upper()
            if code == settings.DISCOUNT_CODE:
                discount = True
                request.session['discount_code'] = code
    #####

    template = 'cart/cart.html'
    context = {
        'discount': discount,
    }

    return render(request, template, context)


def add_to_cart(request, item_id):
    """ Add a product to the cart """

    product = get_object_or_404(Product, pk=item_id)
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
        product = get_object_or_404(Product, pk=item_id)
        cart = request.session.get('cart', {})
        cart.pop(item_id)
        messages.success(request, f'Removed {product.name} from your cart')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
