from django import forms

from order.models import Order
from account.models import User
from cart.models import Cart
from address.models import Address

ADDRESS_TYPES = (
    ('billing', 'Billing address'),
    ('delivery', 'Delivery address'),
)

class OrderForm(forms.ModelForm):
    delivery_address    = forms.ChoiceField(choices=ADDRESS_TYPES)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['shipping_cost'].widget.attrs={'disabled': 'true'}
        self.fields['total'].widget.attrs={'disabled': 'true'}

    class Meta:
        model = Order
        fields='__all__'
        # widgets = {'user': forms.HiddenInput()
        #             ,'cart': forms.HiddenInput()
        #             ,'active': forms.HiddenInput()
        #             ,'status':forms.HiddenInput()
        #           }

