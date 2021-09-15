#from .models import User as CustomUser
from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=150, required=True)
    phone_number = forms.CharField(max_length=17,required=True)
    class Meta:
        model = get_user_model()
        fields = "__all__"
        #fields = ["email","phone_number"]
        exclude = ["is_active","staff", "admin","last_login","address","password"]
        #exclude = ["last_login"]

class LoginForm(forms.Form):
    email = forms.EmailField(label="Email")
    #phone_number = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
