from django import forms
from product.models import Product

class ProductForm(forms.Form):
    class Meta:
        model = Product