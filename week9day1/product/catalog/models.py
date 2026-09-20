from django.db import models


class Product(models.Model):

    class Category(models.TextChoices):
        ELECTRONICS = "EL", "Electronics"
        CLOTHING = "CL", "Clothing"
        FOOD = "FD", "Food"

    sku = models.CharField(
        max_length=50,
        unique=True
    )

    name = models.CharField(
        max_length=120
    )

    description = models.TextField(
        blank=True
    )

    category = models.CharField(
        max_length=2,
        choices=Category.choices,
        default=Category.ELECTRONICS
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    stock = models.PositiveIntegerField(
        default=0
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.name