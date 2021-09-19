from django.conf.urls import url, include
from django.urls import reverse
from product import views

urlpatterns = [
    url(r"^$", views.ProductAllView.as_view(), name="details"),
    url(r'^(?P<pk>[\d]+)/$', views.per_product_view, name='per_product_detail'),
    url(r'^create/$', views.ProductCreateView.as_view(), name='create'),
    url(r'^update/(?P<pk>[\d]+)/$', views.ProductUpdateView.as_view(), name='update'),
    url(r'^delete/(?P<pk>[\d]+)/$', views.ProductDeleteView.as_view(), name='delete')
]
