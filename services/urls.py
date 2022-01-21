from django.conf.urls import url, include
from django.urls import reverse
from services import views

urlpatterns = [
    url(r"^$", views.ServicesAllView.as_view(), name="details"),
    url(r'^(?P<pk>[\d]+)/$', views.per_services_view, name='per_services_detail'),
    url(r'^create/$', views.ServicesCreateView.as_view(), name='create'),
    url(r'^update/(?P<pk>[\d]+)/$', views.ServicesUpdateView.as_view(), name='update'),
    url(r'^delete/(?P<pk>[\d]+)/$', views.ServicesDeleteView.as_view(), name='delete')
]
