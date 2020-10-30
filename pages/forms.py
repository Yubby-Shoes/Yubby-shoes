from django import forms
from store.models import OrderItem, Product
from django.shortcuts import get_object_or_404


class UserDetailForm(forms.Form):
    full_name = forms.CharField(max_length=255)
    phone_number = forms.CharField(max_length=15)
    email = forms.EmailField(required=False)
    address = forms.CharField(max_length=255, widget=forms.Textarea)
    quantity = forms.IntegerField(required=True, widget=forms.NumberInput)

    full_name.widget.attrs.update({
        'placeholder': 'Full Name'
    })
    phone_number.widget.attrs.update({
        'placeholder': 'Phone'
    })
    email.widget.attrs.update({
        'placeholder': 'Email(Optional)'
    })
    address.widget.attrs.update({
        'placeholder': 'Address',
        'rows': 4
    })
    quantity.widget.attrs.update({
        'placeholder': 'Quantity',
        'value': 1
    })

    def clean_quantity(self):
        qty = self.cleaned_data['quantity']
        if not isinstance(qty, int):
            raise forms.ValidationError('Quantity must be an integer')
        return qty

    def save(self, product_id):
        product = get_object_or_404(Product, pk=product_id)
        order_item = OrderItem()
        order_item.product = product
        order_item.order_name = self.cleaned_data['full_name']
        order_item.order_address = self.cleaned_data['address']
        order_item.order_email = self.cleaned_data['email']
        order_item.order_quantity = self.cleaned_data['quantity']
        order_item.order_phone = self.cleaned_data['phone_number']
        order_item.save()
        return order_item
