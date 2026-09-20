# Product Model – Django Guided Lab

A simple Django guided lab for creating a `Product` model and practicing Django model fields.

## Lab Goals

* Create a `catalog` Django app.
* Add the app to `INSTALLED_APPS`.
* Create a `Product` model.
* Use different Django model fields.
* Add category choices using `TextChoices`.
* Run Django checks and migrations.

## Technologies

* Python
* Django
* SQLite

## Project Structure

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

## Product Fields

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

## Setup

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

## Category Choices

The model uses Django `TextChoices` with three categories:

```python
class Category(models.TextChoices):
    ELECTRONICS = "EL", "Electronics"
    CLOTHING = "CL", "Clothing"
    FOOD = "FD", "Food"
```

## Important Concepts

### DecimalField

`DecimalField` is used for the product price because it provides accurate decimal values for monetary amounts.

```python
price = models.DecimalField(
    max_digits=10,
    decimal_places=2
)
```

### blank=True

The description uses `blank=True` because the description is optional.

```python
description = models.TextField(
    blank=True
)
```

## Commands Used

```bash
python manage.py startapp catalog
python manage.py check
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## Learning Outcome

By completing this lab, you practice creating a Django model and using common field types such as `CharField`, `TextField`, `DecimalField`, `BooleanField`, `PositiveIntegerField`, and `DateTimeField`.

Available next action: Create a downloadable DOCX file here in this chat containing the editable prose above
