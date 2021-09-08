from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import login, authenticate, logout
from pdb import set_trace
from .forms import LoginForm
# Create your views here.

def login_page(request):
    context = {"message": "You have reached the Login page."}
    context["form"]=LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            return redirect("home")
    return render(request, "login.html", context)

def signup(request):
    context = {"message": "You have reached the Sign up page."}
    context['form']=SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            full_name = form.cleaned_data.get('full_name')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=full_name, password=raw_password)
            login(request, user)
            return redirect("home")
    return render(request,'signup.html',context)


def user_profile(request):
    context = {"message": "You have been reached the profile page."}
    return render(request, "page_404.html", context)

def home(request):
    context = {"message": "You have been reached the home page."}
    return render(request, "index.html", context)

def logout_page(request):
    context = {"message": "You have been logged out."}
    return render(request, "index.html", context)