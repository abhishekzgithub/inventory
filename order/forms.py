from django import forms

from order.models import Order, OrderItem
from account.models import User
from cart.models import Cart
from address.models import Address

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields='__all__'

class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields='__all__'

