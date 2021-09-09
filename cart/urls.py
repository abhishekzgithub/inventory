from django.conf.urls import url, include
from cart.views import cart_view, cart_update, cart_delete

urlpatterns = [
    url("^$", cart_view, name="cart_page"),
    url("^cart_update/$", cart_update, name="cart_update"),
    url("^cart_delete/$", cart_delete, name="cart_delete"),
]