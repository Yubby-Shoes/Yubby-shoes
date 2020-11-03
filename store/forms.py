from django import forms

from .models import Product, OrderItem


class ProductInfoModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'discounted_price',
                  'image', 'in_stock', 'product_model', 'category', 'company', 'is_new_arrival']


class OrderStatusUpdateForm(forms.ModelForm):
    # order_status = forms.CharField(widget=forms.Select(attrs={}))

    class Meta:
        model = OrderItem
        fields = ['order_status', ]
