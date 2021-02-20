from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from products.models import Product
from .forms import ReviewForm
from datetime import datetime


@login_required
def add_product_review(request, product_id):
    """ A view to create a new product review """
    product = get_object_or_404(Product, pk=product_id)
    user = request.user

    if not request.user:
        messages.error(request, 'Sorry, only registered users can do that!')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid:
            form = form.save(commit=False)
            form.product = product
            form.user = user
            form.timestamp = datetime.now()
            form.save()
            messages.success(request, 'Successfully added review!')
            return redirect(reverse('product_detail', args=[product.id]))
    else:
        form = ReviewForm()

    template = 'reviews/add_product_review.html'

    context = {
        'product': product,
        'form': form,
    }

    return render(request, template, context)
