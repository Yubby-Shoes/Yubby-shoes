from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=20)
    category_initials = models.CharField(max_length=3)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category_name


class Company(models.Model):
    company_name = models.CharField(max_length=100)
    company_initials = models.CharField(max_length=5)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField(default=0.00)
    discounted_price = models.FloatField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    in_stock = models.IntegerField(default=0)
    product_model = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.product_model + '-' + self.name


