# Generated by Django 3.1.2 on 2020-11-03 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_orderitem_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_new_arrival',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]