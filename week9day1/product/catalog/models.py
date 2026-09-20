from django.db import models


class Product(models.Model):

    class Category(models.TextChoices):
        ELECTRONICS = "Electronics", "Electronics"
        CLOTHING = "Clothing", "Clothing"
        FOOD = "Food", "Food"

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
        max_length=20,
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
        return f"{self.name}({self.sku})"