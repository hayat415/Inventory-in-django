# Generated by Django 5.0 on 2024-01-02 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_product_price_sale'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.RemoveField(
            model_name='product',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='sale',
            name='price',
        ),
        migrations.DeleteModel(
            name='Stock',
        ),
    ]
