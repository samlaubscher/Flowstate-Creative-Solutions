from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """ Full Contact form ommiting responded field """

    class Meta:
        model = Contact
        fields = [
            'contact_motive',
            'product_sku',
            'name',
            'user',
            'email',
            'main_message',
        ]
