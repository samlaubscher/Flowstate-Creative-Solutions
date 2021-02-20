from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'contact_motive',
        'product_sku',
        'user',
        'email',
        'main_message',
        'responded',
    )


admin.site.register(Contact, ContactAdmin)
