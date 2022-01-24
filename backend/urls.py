"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.views.i18n import JavaScriptCatalog

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'),name="home"),
    path('jsi18n', JavaScriptCatalog.as_view(), name='js-catlog'),
    path('admin/', admin.site.urls),
    url("^account/",include(("account.urls","account"), namespace="account")),
    url("^product/",include(("product.urls","product"), namespace="product")),
    url("^order/",include(("order.urls","order"), namespace="order")),
    url("^analytics/",include(("analytics.urls","analytics"), namespace="analytics")),
]

#urlpatterns += staticfiles_urlpatterns()

#urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
handler404 = "account.views.error_404"