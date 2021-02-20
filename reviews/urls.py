from django.urls import path
from . import views


urlpatterns = [
    path(
        '<int:product_id>/add_product_review/',
        views.add_product_review,
        name='add_product_review'
    ),
]
