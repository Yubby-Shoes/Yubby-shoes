# Generated by Django 3.1.2 on 2020-11-03 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_product_is_new_arrival'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='is_new_arrival',
            field=models.BooleanField(default=False),
        ),
    ]
