# Generated by Django 4.2.6 on 2023-11-09 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='category',
        ),
    ]
