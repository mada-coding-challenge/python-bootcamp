# Product Model – Django Guided Labs

A simple Django project containing two guided labs for creating and strengthening a `Product` model.

## Lab 1 – Product Model

### Lab Goals

* Create a `catalog` Django app.
* Add the app to `INSTALLED_APPS`.
* Create a `Product` model.
* Use different Django model fields.
* Add category choices using `TextChoices`.
* Run Django checks and migrations.

### Technologies

* Python
* Django
* SQLite

### Project Structure

```text
project/
│
├── manage.py
├── project/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
└── catalog/
    ├── migrations/
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── tests.py
    └── views.py
```

### Product Fields

The `Product` model contains:

| Field         | Type                   | Purpose                      |
| ------------- | ---------------------- | ---------------------------- |
| `sku`         | `CharField`            | Unique product SKU           |
| `name`        | `CharField`            | Product name                 |
| `description` | `TextField`            | Optional product description |
| `category`    | `CharField`            | Product category             |
| `price`       | `DecimalField`         | Product price                |
| `stock`       | `PositiveIntegerField` | Available stock              |
| `is_active`   | `BooleanField`         | Product active status        |
| `created_at`  | `DateTimeField`        | Creation date                |
| `updated_at`  | `DateTimeField`        | Last update date             |

### Setup

Create the app:

```bash
python manage.py startapp catalog
```

Add `catalog` to `INSTALLED_APPS` in `settings.py`.

Then run:

```bash
python manage.py check
```

Create migrations:

```bash
python manage.py makemigrations
```

Apply migrations:

```bash
python manage.py migrate
```

Run the development server:

```bash
python manage.py runserver
```

### Category Choices

The model uses Django `TextChoices` with three categories:

```python
class Category(models.TextChoices):
    ELECTRONICS = "EL", "Electronics"
    CLOTHING = "CL", "Clothing"
    FOOD = "FD", "Food"
```

### Important Concepts

#### DecimalField

`DecimalField` is used for the product price because it provides accurate decimal values for monetary amounts.

```python
price = models.DecimalField(
    max_digits=10,
    decimal_places=2
)
```

#### blank=True

The description uses `blank=True` because the description is optional.

```python
description = models.TextField(
    blank=True
)
```

### Commands Used

```bash
python manage.py startapp catalog
python manage.py check
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

---

# Lab 2 – Strengthen the Product Model

The second lab builds on the `Product` model from Lab 1 by adding behavior, metadata, indexes, and database constraints.

### Lab Goals

* Add an `is_available()` method.
* Add an `inventory_value()` method.
* Set default ordering.
* Add singular and plural verbose names.
* Add a composite database index.
* Add a database constraint for non-negative prices.
* Add a database constraint for non-negative stock.
* Run Django checks and migrations.

## Product Methods

### `is_available()`

Checks whether a product is active and has stock.

```python
def is_available(self):
    return self.is_active and self.stock > 0
```

Example:

```python
product.is_available()
```

Returns:

```text
True
```

when the product is active and has stock.

### `inventory_value()`

Calculates the total value of the available stock.

```python
def inventory_value(self):
    return self.price * self.stock
```

For example:

```text
Price = 50
Stock = 10

Inventory Value = 500
```

## Model Metadata

Default ordering is set by category and then name:

```python
class Meta:
    ordering = ["category", "name"]
```

Clear singular and plural names are also added:

```python
verbose_name = "Product"
verbose_name_plural = "Products"
```

## Composite Index

A composite index is added for `category` and `is_active`:

```python
indexes = [
    models.Index(
        fields=["category", "is_active"]
    ),
]
```

This is useful for queries that commonly use both fields.

For example:

```python
Product.objects.filter(
    category="EL",
    is_active=True
)
```

## Database Constraints

### Price Constraint

The price must be zero or greater:

```python
models.CheckConstraint(
    condition=Q(price__gte=0),
    name="product_price_non_negative"
)
```

### Stock Constraint

The stock must be zero or greater:

```python
models.CheckConstraint(
    condition=Q(stock__gte=0),
    name="product_stock_non_negative"
)
```

The model imports `Q` from Django:

```python
from django.db.models import Q
```

## Complete `Meta` Class

The final `Meta` class is:

```python
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
```

## Lab 2 Commands

After modifying the model, run:

```bash
python manage.py check
```

Create a new migration:

```bash
python manage.py makemigrations
```

Apply the migration:

```bash
python manage.py migrate
```

You can test the model using:

```bash
python manage.py shell
```

## Testing the Methods

Create a product:

```python
from catalog.models import Product

product = Product.objects.create(
    sku="EL-001",
    name="Wireless Mouse",
    category=Product.Category.ELECTRONICS,
    price=50.00,
    stock=10
)
```

Test availability:

```python
product.is_available()
```

Test inventory value:

```python
product.inventory_value()
```

Expected inventory value:

```text
Decimal('500.00')
```

## Why Use Validation and Database Constraints?

`PositiveIntegerField` provides Django-level validation for stock:

```python
stock = models.PositiveIntegerField(default=0)
```

The database constraint provides an additional layer of protection:

```python
models.CheckConstraint(
    condition=Q(stock__gte=0),
    name="product_stock_non_negative"
)
```

This helps ensure that negative stock cannot be stored in the database.

## Learning Outcome

By completing both labs, you practice:

* Creating Django models.
* Using common Django field types.
* Using `TextChoices`.
* Setting default field values.
* Creating model methods.
* Setting model metadata.
* Creating database indexes.
* Creating database constraints.
* Running migrations.
* Testing models using the Django shell.
* Understanding the difference between Django validation and database-level protection.
