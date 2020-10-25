from django import forms


class UserDetailForm(forms.Form):
    full_name = forms.CharField(max_length=255)
    phone_number = forms.CharField(max_length=15)
    email = forms.EmailField(required=False)
    address = forms.CharField(max_length=255, widget=forms.Textarea)

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