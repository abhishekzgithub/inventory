from django.conf.urls import url, include
from address import views

urlpatterns = [
    url("^create/$", views.AddressCreateView.as_view(), name="create_address"),
    url(r'^delete/(?P<id>[\d]+)/$', views.delete_address, name="delete_address"),
    url("^update/$", views.update_address, name="update_address"),
    #url("^$", views.AddressDetails.as_view(), name="view_address"),
    
]