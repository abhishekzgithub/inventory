from django.shortcuts import render, redirect
from account.forms import SignUpForm, LoginForm, UserProfileForm, UserPasswordChangeForm
from django.contrib.auth import login, authenticate, logout, views
from django.views.generic import FormView, DetailView
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from account.models import User
from django.conf import settings

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
            context["error"]=form.error_messages
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
            context["errors"]=form.error_messages
            print(form.errors)
            print(form.error_messages)
    return render(request,'signup.html',context)


class UserProfile(DetailView):
    template_name="user_profile.html"
    form_class= UserProfileForm
    model = User
    success_url = "/account/profile"
    def get_context_data(self, **kwargs):
        context = super(UserProfile, self).get_context_data(**kwargs)
        context['form'] = UserProfileForm
        return context

@login_required(login_url=settings.LOGIN_URL)
def password_change(request):
    from django.contrib.auth import update_session_auth_hash
    if request.method == 'POST':
        form = UserPasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)



def home(request):
    context = {"message": "You have been reached the home page."}
    return render(request, "index.html", context)

def logout_page(request):
    context = {"message": "You have been logged out."}
    return views.logout_then_login(request, login_url=settings.LOGIN_URL)

def error_404(request, exception):
    context={"data":exception}
    return render(request, "page_404.html", context)