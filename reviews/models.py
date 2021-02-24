from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Review(models.Model):
    """ A model for Reviews """
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='review'
    )
    user = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=False, null=False)
    body = models.TextField(max_length=600, blank=False, null=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        return 'Review {} by {}'.format(self.title, self.user)
