from django.shortcuts import render, redirect
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy, reverse
from product.forms import ProductForm
from product.models import Product
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from django.db.models import Q


@login_required(login_url=settings.LOGIN_URL)
def per_category_product_view(request,category1,category2, pk):
    context={"products":""}
    if request.method=="GET":
        context["products"] = Product.objects.filter(category1=category1, category2=category2, pk=pk).all()
    return render(request, "product/per_product_details.html", context)


class ProductAllView(LoginRequiredMixin, View):
    login_url = settings.LOGIN_URL
    def get(self, request, context={}):
        if request.user and (not request.user.is_anonymous) and (request.user.email) and (request.user.is_authenticated):
            context={"product":None}
            context = {"message": "{} has reached the Product page.".format(request.user)}
            context["products"]=Product.objects.all()
        return render(request, "product/product_details.html", context)

class ProductDetailView(LoginRequiredMixin, DetailView):
    login_url       = settings.LOGIN_URL
    model			= Product
    fields			= "__all__"
    template_name	= 'product/product.html'
    success_url		= reverse_lazy('product:details')

class ProductCreateView(LoginRequiredMixin, CreateView):
    login_url       = settings.LOGIN_URL
    model			= Product
    form_class      = ProductForm
    template_name	= 'product/create_product.html'
    success_url		= reverse_lazy('product:details')


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    login_url       = settings.LOGIN_URL
    model			= Product
    #form_class      = ProductForm
    fields			= "__all__"
    template_name	= 'product/product_update_form.html'
    template_name_suffix = '_update_form'
    success_url		= reverse_lazy('product:details')


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    login_url       = settings.LOGIN_URL
    model			= Product
    form_class      = ProductForm
    template_name	= 'product/product_confirm_delete.html'
    success_url		= reverse_lazy('product:details')
