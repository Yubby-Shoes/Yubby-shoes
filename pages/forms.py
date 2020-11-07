from django import forms
from store.models import OrderItem, Product
from accounts.models import Customer
from django.shortcuts import get_object_or_404


class UserDetailForm(forms.Form):
    customer_model = Customer
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
        customer_with_phone = self.customer_model.objects.all()
        customer_phone = self.cleaned_data['phone_number']
        customer_name = self.cleaned_data['full_name']
        customer_address = self.cleaned_data['address']
        try:
            c = customer_with_phone.get(phone_number=customer_phone)
        except customer_with_phone.model.DoesNotExist:
            c = self.customer_model()
            c.name = customer_name
            c.address = customer_address
            c.phone_number = customer_phone
            c.save()
        # if not customer_with_phone:
        #     c = self.customer_model()
        #     c.name = customer_name
        #     c.address = customer_address
        #     c.phone_number = customer_phone
        #     c.save()
        order_item.customer = c
        order_item.product = product
        order_item.order_name = customer_name
        order_item.order_address = customer_address
        order_item.order_email = self.cleaned_data['email']
        order_item.order_quantity = self.cleaned_data['quantity']
        order_item.order_phone = customer_phone
        order_item.save()

        return order_item

