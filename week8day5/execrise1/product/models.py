
# Create your models here.
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=120)

    is_active = models.BooleanField(default=True)

    available_from = models.DateField()

    description = models.TextField()

    price = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    created_at = models.DateTimeField(auto_now_add=True)

    stock = models.PositiveIntegerField(default=0)

    product_image = models.ImageField(upload_to="products/")