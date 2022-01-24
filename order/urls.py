from django.conf.urls import url, include
import order.views as order_views

urlpatterns = [
    
    url("^$", order_views.OrderView.as_view(), name="details"),
    url(r"^add/(?P<pk>[\d]+)/$", order_views.OrderView.as_view(), name="add_to_cart"),
    url(r'^update/(?P<pk>[\d]+)/$', order_views.OrderItemUpdateView.as_view(), name="update_cart_item"),
    url(r'^delete/(?P<pk>[\d]+)/$', order_views.OrderItemDeleteView.as_view(), name="delete_from_cart"),

    url(r"^submit_order/(?P<pk>[\d]+)/$", order_views.OrderSubmitView.as_view(), name="submit_order"),
]