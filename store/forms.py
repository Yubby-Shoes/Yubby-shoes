from django.forms import ModelForm

from .models import Product


class ProductInfoModelForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'discounted_price',
                  'image', 'in_stock', 'product_model']
