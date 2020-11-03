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
        prev_status = OrderItem.objects.get(pk=self.instance.id).order_status
        if self.instance.product.in_stock > 0:
            if prev_status == 'PR':
                self.instance.product.in_stock -= self.instance.order_quantity
                self.instance.product.save()
        return super().save()
