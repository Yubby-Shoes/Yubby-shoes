from django.contrib import admin
from .models import Product, Company, Category

# Register your models here.

admin.site.register(Product)
admin.site.register(Company)
admin.site.register(Category)
