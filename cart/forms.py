# from .models import User as CustomUser
from django import forms
from django.contrib.auth.forms import UserCreationForm

# class SignUpForm(UserCreationForm):
#     class Meta:
#         model = CustomUser
#         fields = ["email","full_name","phone_number"]
#         exclude = ["is_active","staff", "admin","last_login"]

# class LoginForm(forms.Form):
#     email = forms.EmailField(label="Email")
#     #phone_number = forms.CharField()
#     password = forms.CharField(widget=forms.PasswordInput)
