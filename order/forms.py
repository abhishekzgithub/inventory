from django import forms
from order.models import Order

class OrderForm(forms.ModelForm):
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

