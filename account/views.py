from django.shortcuts import render, redirect
from account.forms import SignUpForm, LoginForm
from django.contrib.auth import login, authenticate, logout

# Create your views here.

def login_page(request):
    context = {"message": "You have reached the Login page."}
    context["form"]=LoginForm(request)
    if request.method == "POST":
        form = LoginForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            if user:
                login(request, user)
                return redirect("home")
        else:
            print(form.errors)
            print(form.error_messages)
    return render(request, "login.html", context)

def signup(request):
    context = {"message": "You have reached the Sign up page."}
    context['form']=SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            if user:
                login(request, user)
                return redirect("home")
        elif form.errors:
            context["errors"]=form.errors
            print(form.errors)
            print(form.error_messages)
    return render(request,'signup.html',context)


def user_profile(request):
    context = {"message": "You have been reached the profile page."}
    return render(request, "page_404.html", context)

def home(request):
    context = {"message": "You have been reached the home page."}
    return render(request, "index.html", context)

def logout_page(request):
    context = {"message": "You have been logged out."}
    logout(request)
    return render(request, "index.html", context)