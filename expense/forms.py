from django import forms

from expense.models import Expense

class ExpenseForm(forms.ModelForm):    
    class Meta:
        model = Expense
        fields = "__all__"
        exclude = ['user']

