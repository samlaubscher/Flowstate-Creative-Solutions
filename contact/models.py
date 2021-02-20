from django.db import models


CONTACT_MOTIVES = (
    ('general_enquiry', 'General Enquiry'),
    ('product_technical_assistance', 'Product Technical Assistance'),
    ('product_suggestion', 'Product Suggestion'),
    ('general_feedback', 'General Feedback'),
)


class Contact(models.Model):
    """ A model for contact submissions """

    class Meta:
        verbose_name_plural = 'Contact Page Submissions'

    contact_motive = models.CharField(
        max_length=120,
        choices=CONTACT_MOTIVES,
        default='general_enquiry',
        null=False,
        blank=False,
    )
    product_sku = models.CharField(
        max_length=20,
        null=True,
        blank=True,
    )
    name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
    )
    email = models.CharField(
        max_length=90,
        null=False,
        blank=False,
    )
    main_message = models.TextField(
        max_length=3000,
        null=False,
        blank=False,
    )
    responded = models.BooleanField(default=False)

    def __str__(self):
        return self.name
