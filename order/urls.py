from django.conf.urls import url, include
import order.views as order_views

urlpatterns = [
    #url("^$", order_views.order_view, name="order_view"),
    url("^$", order_views.OrderItemAllView.as_view(), name="details"),
    # url("^create_order$", order_views.create_order, name="create_order"),
    #url("^$", order_views.get_orders, name="details"),
    
    url("^create$", order_views.OrderItemCreateView.as_view(), name="create"),
    url(r'^update/(?P<pk>[\d]+)/$', order_views.OrderItemUpdateView.as_view(), name="update"),
    url(r'^delete/(?P<pk>[\d]+)/$', order_views.OrderItemDeleteView.as_view(), name="delete"),
    url("^submit$", order_views.submit_form, name="submit"),
]