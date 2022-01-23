from django import forms

from order.models import Order, OrderItem

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields='__all__'

class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields='__all__'

