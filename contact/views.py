from django.shortcuts import render, reverse, redirect
from django.contrib import messages
from .forms import ContactForm


def contact(request):
    """ A view to return the contact page """

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Your message has been successfully sent!'
            )
            return redirect(reverse('contact'))
        else:
            messages.error(
                request,
                'Your message failed to send. \
                Please check the form is valid and try again.'
            )

    else:
        form = ContactForm()

    template = 'contact/contact.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
