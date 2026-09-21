from django.db import models
from django.db.models import Q
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
    
    def is_available(self):
            return self.is_active and self.stock > 0

    def inventory_value(self):
        return self.price * self.stock

    class Meta:

        ordering = ["category", "name"]

        verbose_name = "Product"
        verbose_name_plural = "Products"

        indexes = [
            models.Index(
                fields=["category", "is_active"]
            ),
        ]

        constraints = [
            models.CheckConstraint(
                condition=Q(price__gte=0),
                name="product_price_non_negative"
            ),

            models.CheckConstraint(
                condition=Q(stock__gte=0),
                name="product_stock_non_negative"
            ),
        ]