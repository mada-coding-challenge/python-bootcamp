from django.db import migrations

def populate_code(apps, schema_editor):
    Product = apps.get_model('products', 'Product')
    for product in Product.objects.all():
        product.code = f"PROD-{product.id}"
        product.save()

def reverse_populate_code(apps, schema_editor):
    Product = apps.get_model('products', 'Product')
    Product.objects.all().update(code=None)

class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_add_product_code_nullable'),
    ]

    operations = [
        migrations.RunPython(populate_code, reverse_populate_code),
    ]