# Django Guided Lab: Product Search QuerySet

A beginner-friendly Django lab focused on building reusable database queries using Django ORM and QuerySets.

The goal of this lab is to create a reusable product search function that filters, searches, orders, and retrieves product data without writing raw SQL queries.

## Learning Objectives

By completing this lab, I practiced:

* Filtering active products using `filter()`.
* Filtering products based on stock availability.
* Searching multiple fields using `Q` objects.
* Applying optional minimum and maximum price filters.
* Filtering through ForeignKey relationships.
* Ordering QuerySets using multiple fields.
* Limiting results using QuerySet slicing.
* Selecting specific fields using `values()`.
* Understanding QuerySet refinement and evaluation.

## Technologies Used

* Python
* Django
* SQLite
* Django ORM

## Project Structure

```text
product_search_lab/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── catalog/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── queries.py
│   ├── tests.py
│   └── views.py
│
├── manage.py
└── README.md
```

## Models

### Category

Represents a product category.

### Product

Contains the following fields:

| Field     | Description                         |
| --------- | ----------------------------------- |
| name      | Product name                        |
| sku       | Unique product identifier           |
| price     | Product price                       |
| stock     | Available quantity                  |
| is_active | Product availability                |
| category  | ForeignKey relationship to Category |

Relationship:

One Category can have multiple Products (One-to-Many).

## Main Feature: Reusable Search Function

The main implementation is located in `catalog/queries.py`.

The `search_products()` function supports:

1. Returning active products only.
2. Excluding products with zero stock.
3. Searching product names or SKUs.
4. Filtering by optional price range.
5. Filtering by category name through a ForeignKey relationship.
6. Ordering results by price, name, and primary key.

### Example

```python
from django.db.models import Q
from .models import Product


def search_products(
    query=None,
    min_price=None,
    max_price=None,
    category_name=None
):
    products = Product.objects.filter(is_active=True)

    products = products.filter(stock__gt=0)

    if query:
        products = products.filter(
            Q(name__icontains=query) |
            Q(sku__icontains=query)
        )

    if min_price is not None:
        products = products.filter(price__gte=min_price)

    if max_price is not None:
        products = products.filter(price__lte=max_price)

    if category_name:
        products = products.filter(
            category__name__iexact=category_name
        )

    products = products.order_by('price', 'name', 'pk')

    return products
```

## Setup Instructions

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd product_search_lab
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
```

### 3. Activate the environment

macOS / Linux:

```bash
source venv/bin/activate
```

### 4. Install Django

```bash
pip install django
```

### 5. Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Run the development server

```bash
python manage.py runserver
```

## Testing with Django Shell

Open the Django shell:

```bash
python manage.py shell
```

Import the function:

```python
from catalog.queries import search_products
```

### Search all available products

```python
products = search_products()
```

### Search by keyword

```python
products = search_products(query="lap")
```

### Filter by price range

```python
products = search_products(
    min_price=100,
    max_price=5000
)
```

### Filter by category

```python
products = search_products(category_name="Laptops")
```

### Combine filters

```python
products = search_products(
    query="lap",
    min_price=1000,
    max_price=5000,
    category_name="Laptops"
)
```

### Get the first 10 products

```python
products = search_products()[:10]
```

### Return selected fields

```python
result = search_products().values(
    'name',
    'sku',
    'price'
)[:10]

print(list(result))
```

## Key Concepts Learned

| Concept               | Django ORM       |
| --------------------- | ---------------- |
| Retrieve records      | `objects.all()`  |
| Filter records        | `filter()`       |
| Greater than          | `__gt`           |
| Greater than or equal | `__gte`          |
| Less than or equal    | `__lte`          |
| OR conditions         | `Q() \| Q()`     |
| Relationship lookup   | `category__name` |
| Sorting               | `order_by()`     |
| Limit results         | `[:10]`          |
| Select fields         | `values()`       |
| Check existence       | `exists()`       |

## QuerySet Refinement vs Evaluation

An important concept from this lab is that Django QuerySets are lazy.

**Refinement:** Builds or modifies a QuerySet without immediately retrieving the results.

Examples:

```python
Product.objects.filter(is_active=True)
products.order_by('price')
products.values('name', 'price')
products[:10]
```

**Evaluation:** Executes the query when results are needed.

Examples:

```python
list(products)
```

```python
for product in products:
    print(product.name)
```

```python
products.count()
products.exists()
```

## What I Learned

This lab helped me understand how Django ORM can build flexible and reusable database queries.

Instead of repeating filtering logic, I learned how to create one function that accepts optional parameters and returns a QuerySet that can be further refined or evaluated when needed.

It also strengthened my understanding of `Q` objects, ForeignKey relationships, QuerySet laziness, and retrieving only the fields required.

---

**Tuwaiq Academy — Python & Django Bootcamp**
*Guided Lab: Product Search QuerySet*
