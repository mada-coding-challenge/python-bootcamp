# Django Product Exercise

A simple Django project for practicing **Django Models, Migrations, SQLite, and ImageField**.

## Features

The project contains a `Product` model with:

* Product name
* Active status
* Available date
* Description
* Price
* Creation date
* Stock quantity
* Product image

## Product Model

```python
class Product(models.Model):
    name = models.CharField(max_length=120)
    is_active = models.BooleanField(default=True)
    available_from = models.DateField()
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    stock = models.PositiveIntegerField(default=0)
    product_image = models.ImageField(upload_to="products/")
```

## Project Structure

```text
exercise1/
│
├── manage.py
│
├── product/
│   ├── migrations/
│   ├── files/
│   │   └── images.jpeg
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── src/
│
├── db.sqlite3
│
└── venv/
```

## Requirements

* Python
* Django
* Pillow

Install Django and Pillow:

```bash
pip install django
pip install Pillow
```

## Setup

Activate the virtual environment:

```bash
source venv/bin/activate
```

Run migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

Start the development server:

```bash
python manage.py runserver
```

## Adding a Product Through Django Shell

Open the Django shell:

```bash
python manage.py shell
```

Import the model:

```python
from product.models import Product
```

Create a product:

```python
product = Product.objects.create(
    name="Wireless Headphones",
    is_active=True,
    available_from="2026-09-20",
    description="Wireless headphones with high quality sound.",
    price=249.99,
    stock=10
)
```

## Uploading an Image Through Shell

Import `File`:

```python
from django.core.files import File
```

Then upload the image:

```python
with open("product/files/images.jpeg", "rb") as image:
    product = Product.objects.create(
        name="Wireless Headphones",
        is_active=True,
        available_from="2026-09-20",
        description="Wireless headphones with high quality sound.",
        price=249.99,
        stock=10,
        product_image=File(image, name="images.jpeg")
    )
```

The image will be stored under:

```text
media/
└── products/
    └── images.jpeg
```

## Checking Products

Print all products:

```python
for product in Product.objects.all():
    print(product.name, product.price, product.stock)
```

Check the uploaded image:

```python
print(product.product_image.name)
```

Example:

```text
products/images.jpeg
```

## Media Settings

Add the following to `settings.py`:

```python
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
```

## Technologies

* Python
* Django
* SQLite
* Pillow
* Django ORM
* Django ImageField
