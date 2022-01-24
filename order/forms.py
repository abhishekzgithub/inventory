from django import forms
from django.contrib.admin.widgets import  AdminDateWidget, AdminTimeWidget, AdminSplitDateTime

from order.models import Order, OrderItem

class OrderForm(forms.ModelForm):
    ordered_date = forms.DateField(widget=AdminDateWidget())
    delivery_date = forms.DateField(widget=AdminDateWidget())
    class Meta:
        model = Order
        fields = ["delivery_address", "payment_method",
                    "status","notes"    
                    ]
        #exclude = ["ordered_date","delivery_date"]

class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields='__all__'

