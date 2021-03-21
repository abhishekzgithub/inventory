from django.conf.urls import url, include
from .views import login_page, signup, logout_page #Login, SignUp
from django.contrib.auth.views import LogoutView

urlpatterns = [
    url("^signup/$", signup, name="signup"),
    url("^logout/$", LogoutView.as_view(), name="logout"),
    url("^login/$", login_page, name="login"),
]