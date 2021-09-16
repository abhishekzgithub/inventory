from django.conf.urls import url, include
from address import views

urlpatterns = [
    url("^create/$", views.AddressCreateView.as_view(), name="create_address"),
    url(r'^delete/(?P<pk>[\d]+)/$', views.AddressDeleteView.as_view(), name="delete_address"),
    url(r'^update/(?P<pk>[\d]+)/$', views.AddressUpdateView.as_view(), name="update_address"),
    
]