from django.db.models import Q
from .models import Product


def search_products(
    query=None,
    min_price=None,
    max_price=None,
    category_name=None
):

    # 1. Start with active products
    products = Product.objects.filter(is_active=True)

    # 2. Keep products with stock above zero
    products = products.filter(stock__gt=0)

    # 3. Search name OR SKU
    if query:
        products = products.filter(
            Q(name__icontains=query) |
            Q(sku__icontains=query)
        )

    # 4. Optional minimum price
    if min_price is not None:
        products = products.filter(price__gte=min_price)

    # Optional maximum price
    if max_price is not None:
        products = products.filter(price__lte=max_price)

    # 5. Filter by category name across relationship
    if category_name:
        products = products.filter(
            category__name__iexact=category_name
        )

    # 6. Order by price, name, then primary key
    products = products.order_by('price', 'name', 'pk')


    
    return products

    products = search_products()

    first_ten = products[:10]
    
    products = search_products()

    result = products.values('name', 'sku', 'price')[:10]