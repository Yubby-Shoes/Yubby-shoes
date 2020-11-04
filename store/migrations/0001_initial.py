# Generated by Django 3.1.2 on 2020-11-04 07:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=20)),
                ('category_initials', models.CharField(max_length=3)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('company_initials', models.CharField(max_length=5)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.FloatField(default=0.0)),
                ('discounted_price', models.FloatField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/products')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('is_new_arrival', models.BooleanField(default=False)),
                ('in_stock', models.IntegerField(default=0)),
                ('product_model', models.CharField(max_length=10, unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='store.category')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.company')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered_on', models.DateTimeField(auto_now_add=True)),
                ('order_name', models.CharField(max_length=255)),
                ('order_address', models.CharField(max_length=255)),
                ('order_email', models.CharField(blank=True, max_length=255, null=True)),
                ('order_phone', models.CharField(max_length=14)),
                ('order_quantity', models.IntegerField()),
                ('order_status', models.CharField(choices=[('PR', 'Processing'), ('SH', 'Shipping'), ('DE', 'Delivered')], default='PR', max_length=3)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='store.product')),
            ],
        ),
    ]
