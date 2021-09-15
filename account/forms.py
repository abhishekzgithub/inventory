#from .models import User as CustomUser
from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=150, required=True)
    phone_number = forms.CharField(max_length=17,required=True)
    class Meta:
        model = get_user_model()
        fields = "__all__"
        exclude = ["is_active","staff", "admin","last_login","address","password"]


class LoginForm(AuthenticationForm):
    pass