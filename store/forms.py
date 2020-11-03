from django import forms

from .models import Product, OrderItem


class ProductInfoModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'discounted_price',
                  'image', 'in_stock', 'product_model', 'category', 'company']


class OrderStatusUpdateForm(forms.ModelForm):
    # order_status = forms.CharField(widget=forms.Select(attrs={}))

    class Meta:
        model = OrderItem
        fields = ['order_status', ]

    def save(self, commit=True):
        print(self.instance.product.in_stock)
        print(self.instance.order_status)
        if self.instance.product.in_stock > 0:
            if self.instance.order_status == 'PR':
                self.instance.product.in_stock -= self.object.order_quantity
                self.instance.product.save()
        return super().save()
