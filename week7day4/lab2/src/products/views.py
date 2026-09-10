from django.shortcuts import render

from django.core.paginator import Paginator

products = [
    {
        "id": 1,
        "name": "Laptop",
        "category": "electronics",
        "price": 999.99,
        "rating": 4.5,
        "description": "Powerful laptop for work, study, and everyday use.",
    },
    {
        "id": 2,
        "name": "Wireless Headphones",
        "category": "electronics",
        "price": 149.99,
        "rating": 4.3,
        "description": "Comfortable wireless headphones with noise cancellation.",
    },
    {
        "id": 3,
        "name": "Running Shoes",
        "category": "fashion",
        "price": 89.99,
        "rating": 4.6,
        "description": "Lightweight running shoes designed for everyday training.",
    },
    {
        "id": 4,
        "name": "Backpack",
        "category": "accessories",
        "price": 49.99,
        "rating": 4.2,
        "description": "Durable backpack with multiple compartments.",
    },
    {
        "id": 5,
        "name": "Smart Watch",
        "category": "electronics",
        "price": 199.99,
        "rating": 4.4,
        "description": "Smart watch with fitness tracking and notifications.",
    },
    {
        "id": 6,
        "name": "Coffee Maker",
        "category": "home",
        "price": 79.99,
        "rating": 4.1,
        "description": "Easy-to-use coffee maker for fresh coffee at home.",
    },
    {
        "id": 7,
        "name": "Desk Lamp",
        "category": "home",
        "price": 34.99,
        "rating": 4.0,
        "description": "Modern LED desk lamp with adjustable brightness.",
    },
    {
        "id": 8,
        "name": "T-Shirt",
        "category": "fashion",
        "price": 24.99,
        "rating": 4.7,
        "description": "Comfortable cotton T-shirt available in multiple sizes.",
    },
    {
        "id": 9,
        "name": "Keyboard",
        "category": "electronics",
        "price": 69.99,
        "rating": 4.5,
        "description": "Mechanical keyboard designed for typing and gaming.",
    },
    {
        "id": 10,
        "name": "Water Bottle",
        "category": "accessories",
        "price": 19.99,
        "rating": 4.3,
        "description": "Reusable stainless steel water bottle.",
    },
]

def sort_by_price(product):
    return product["price"]


def sort_by_rating(product):
    return product["rating"]


def sort_by_name(product):
    return product["name"]

def product_list(request):
    category = request.GET.get("category", "")
    min_price = request.GET.get("min_price", "")
    q = request.GET.get("q", "")
    sort = request.GET.get("sort", "name")

    # Invalid sort falls back to name
    if sort not in ["price", "rating", "name"]:
        sort = "name"

    filtered_products = products

    # Category filter
    if category:
        filtered_products = [
            product
            for product in filtered_products
            if product["category"] == category
        ]

    # Minimum price filter
    if min_price:
        filtered_products = [
            product
            for product in filtered_products
            if product["price"] >= float(min_price)
        ]

    # Search
    if q:
        filtered_products = [
            product
            for product in filtered_products
            if q.lower() in product["name"].lower()
        ]

    # Sorting
    if sort == "price":
        filtered_products = sorted(
            filtered_products,
            key=sort_by_price
        )

    elif sort == "rating":
        filtered_products = sorted(
            filtered_products,
            key=sort_by_rating
        )

    else:
        filtered_products = sorted(
            filtered_products,
            key=sort_by_name
        )

    # Pagination
    paginator = Paginator(filtered_products, 3)

    page_number = request.GET.get("page", 1)

    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "products.html",
        {
            "products": page_obj,
            "page_obj": page_obj,
            "category": category,
            "min_price": min_price,
            "q": q,
            "sort": sort,
        },
    )

def product_detail(request, id):
    for product in products:
        if product["id"] == id:

            tab = request.GET.get("tab", "details")

            if tab not in ["details", "reviews", "shipping"]:
                tab = "details"

            return render(
                request,
                "product_detail.html",
                {
                    "product": product,
                    "tab": tab,
                },
            )

    return render(request, "404.html")