from django.conf.urls import url, include
from .views import cart_view

urlpatterns = [
    url("^$", cart_view, name="cart_page"),
]