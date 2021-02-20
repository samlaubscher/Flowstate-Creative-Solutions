from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    """ Full Review form """

    class Meta:
        model = Review
        fields = [
            'body',
        ]
