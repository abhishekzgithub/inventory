from django.conf.urls import url, include
from .views import product_view, per_product_view

urlpatterns = [
    url("^$", product_view, name="product_page"),
    url(r'^(?P<id>[\w-]+)/$', per_product_view, name='detail'),

]