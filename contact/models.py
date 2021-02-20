from django.db import models


CONTACT_MOTIVES = (
    ('general_enquiry', 'GENERAL ENQUIRY'),
    ('product_technical_assistance', 'PRODUCT TECHNICAL ASSISTANCE'),
    ('product_suggestion', 'PRODUCT SUGGESTION'),
    ('general_feedback', 'GENERAL FEEDBACK'),
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
        null=True,
        blank=True,
    )
    user = models.CharField(
        max_length=50,
        null=False,
        blank=False,
    )
    email = models.CharField(
        max_length=90,
        null=False,
        blank=False,
    )
    main_message = models.CharField(
        max_length=3000,
        null=False,
        blank=False,
    )
    responded = models.BooleanField(default=False)

    def __str__(self):
        return self.name
