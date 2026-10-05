# Catalogue Summary Report – Django Guided Lab

A Django guided lab for practicing ORM queries, grouping, annotations, and aggregations using `Product` and `Category` models.

## Lab Objective

The goal of this lab is to create:

1. A category summary report for active products.
2. An overall summary containing the total number of active products and their average price.

The lab demonstrates the difference between `annotate()` and `aggregate()` and how `values()` can be used to group query results.

---

## Technologies

- Python
- Django
- SQLite
- Django ORM

---

## Models

The project contains two main models:

### Category

```python
class Category(models.Model):
    name = models.CharField(max_length=100)
```

### Product

Each product belongs to a category and contains information such as:

- Name
- Category
- Price
- Stock
- Active status

Example:

```python
class Product(models.Model):
    name = models.CharField(max_length=120)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )
    stock = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
```

---

## Category Summary Report

The category report performs the following operations:

1. Keeps active products only.
2. Groups products by category ID and category name.
3. Counts the number of products in each category.
4. Calculates the average product price for each category.
5. Calculates the total stock for each category.
6. Keeps only categories with at least three active products.
7. Orders categories by product count in descending order and then by category name.

### Query

```python
from django.db.models import Count, Avg, Sum
from .models import Product


def category_summary():
    return (
        Product.objects
        .filter(is_active=True)
        .values("category_id", "category__name")
        .annotate(
            product_count=Count("id"),
            average_price=Avg("price"),
            total_stock=Sum("stock"),
        )
        .filter(product_count__gte=3)
        .order_by("-product_count", "category__name")
    )
```

---

## How the Query Works

### 1. Filter Active Products

```python
.filter(is_active=True)
```

Only active products are included in the report.

### 2. Group by Category

```python
.values("category_id", "category__name")
```

This groups the products using their category ID and category name.

### 3. Count Products

```python
product_count=Count("id")
```

Calculates the number of active products in each category.

### 4. Calculate Average Price

```python
average_price=Avg("price")
```

Calculates the average price of the products in each category.

### 5. Calculate Total Stock

```python
total_stock=Sum("stock")
```

Calculates the total available stock for each category.

### 6. Keep Categories With at Least Three Products

```python
.filter(product_count__gte=3)
```

Only categories containing three or more active products are included.

### 7. Order the Results

```python
.order_by("-product_count", "category__name")
```

Categories are ordered by product count from highest to lowest.

If two categories have the same number of products, they are ordered alphabetically by category name.

---

## Example Data

Example products were created using the Django shell:

```python
electronics = Category.objects.create(name="Electronics")

Product.objects.create(
    name="Laptop",
    category=electronics,
    price=4000,
    stock=5,
    is_active=True
)

Product.objects.create(
    name="Mouse",
    category=electronics,
    price=100,
    stock=20,
    is_active=True
)

Product.objects.create(
    name="Keyboard",
    category=electronics,
    price=200,
    stock=10,
    is_active=True
)
```

The Electronics category therefore contains:

| Product | Price | Stock |
|---|---:|---:|
| Laptop | 4000 | 5 |
| Mouse | 100 | 20 |
| Keyboard | 200 | 10 |

---

## Example Category Report Result

Running:

```python
category_summary()
```

returns a QuerySet similar to:

```python
<QuerySet [
    {
        'category_id': 1,
        'category__name': 'Electronics',
        'product_count': 3,
        'average_price': Decimal('1433.33333333333'),
        'total_stock': 35
    }
]>
```

The result shows that the Electronics category has:

- 3 active products
- Average price of approximately 1433.33
- Total stock of 35

---

## Overall Summary

A separate aggregate query is used to calculate information about all active products.

```python
def overall_summary():
    return (
        Product.objects
        .filter(is_active=True)
        .aggregate(
            total_products=Count("id"),
            average_price=Avg("price"),
        )
    )
```

Example result:

```python
{
    "total_products": 3,
    "average_price": Decimal("1433.33333333333")
}
```

---

## `annotate()` vs `aggregate()`

### `annotate()`

`annotate()` calculates values for each object or group.

In this lab, it calculates information for each category:

```python
.annotate(
    product_count=Count("id"),
    average_price=Avg("price"),
    total_stock=Sum("stock")
)
```

The category report is therefore a QuerySet containing multiple dictionaries.

Example:

```python
[
    {...},
    {...},
    {...}
]
```

### `aggregate()`

`aggregate()` calculates a final summary for the entire QuerySet.

For example:

```python
.aggregate(
    total_products=Count("id"),
    average_price=Avg("price")
)
```

It returns one dictionary:

```python
{
    "total_products": 10,
    "average_price": 250.50
}
```

---

## Why Does `values()` Come Before `annotate()`?

In the category report:

```python
.values("category_id", "category__name")
.annotate(...)
```

`values()` defines how the products should be grouped.

Django first groups products by:

```text
category_id
category__name
```

Then `annotate()` performs calculations such as `Count`, `Avg`, and `Sum` for each group.

Therefore, the query follows this logic:

```text
Filter rows
    ↓
Group by category
    ↓
Calculate values for each group
    ↓
Filter groups
    ↓
Order results
```

This is why `values()` appears before `annotate()` in the category report.

---

## Running the Project

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

Install Django:

```bash
pip install django
```

Apply migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

Open the Django shell:

```bash
python manage.py shell
```

Import the report functions:

```python
from catalog.queries import category_summary, overall_summary
```

Run the category report:

```python
category_summary()
```

Run the overall summary:

```python
overall_summary()
```

---

## Key Concepts Learned

- Filtering QuerySets with `filter()`
- Grouping data with `values()`
- Using `annotate()` for per-group calculations
- Using `aggregate()` for overall calculations
- Counting records with `Count()`
- Calculating averages with `Avg()`
- Calculating totals with `Sum()`
- Filtering annotated values
- Ordering QuerySets with `order_by()`
- Following ForeignKey relationships using `__`
- Understanding the difference between a QuerySet of dictionaries and a single aggregate dictionary

---

## Conclusion

This guided lab demonstrates how Django ORM can be used to create summary reports directly from database data without manually looping through every product.

The category report uses:

```text
filter → values → annotate → filter → order_by
```

while the overall report uses:

```text
filter → aggregate
```

These techniques are useful for building dashboards, reports, statistics, and analytics in Django applications.