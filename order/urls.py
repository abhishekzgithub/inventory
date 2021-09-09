from django.conf.urls import url, include
import order.views as order_views

urlpatterns = [
    url("^$", order_views.get_orders, name="get_orders"),
]