from django import forms
from services.models import Services

class ServicesForm(forms.ModelForm):
    class Meta:
        model = Services
        fields = "__all__"
