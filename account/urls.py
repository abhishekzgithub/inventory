from django.conf.urls import url, include
from account.views import login_page, signup, logout_page, user_profile #Login, SignUp
from django.contrib.auth.views import LogoutView

urlpatterns = [
    url("^signup/$", signup, name="signup"),
    url("^logout/$", logout_page, name="logout"),
    url("^login/$", login_page, name="login"),
    url("^profile/$", user_profile, name="profile"),
]