
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()  
    code = models.CharField(max_length=50, null=False, unique=True)

    def __str__(self):
        return self.name