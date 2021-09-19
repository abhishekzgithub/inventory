from django.shortcuts import render, redirect
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy, reverse
from account.models import User
from product.forms import ProductForm
from product.models import Product
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

def per_product_view(request,pk):
    context={"products":""}
    if request.method=="GET":
        context["products"] = Product.objects.filter(pk=pk).all()
    return render(request, "product/per_product_details.html", context)

class ProductAllView(View):
    def get(self, request, context={}):
        if request.user and (not request.user.is_anonymous) and (request.user.email) and (request.user.is_authenticated):
            context={"product":None}
            context = {"message": "{} has reached the Product page.".format(request.user)}
            product_obj=Product.objects.filter(user=User.objects.get(email=request.user.email))
            if product_obj:
                product_obj=product_obj.all()
                context["products"]=product_obj
        return render(request, "product/product_details.html", context)

class ProductDetailView(DetailView):
    model			= Product
    fields			= "__all__"
    template_name	= 'product/product.html'
    success_url		= reverse_lazy('product:details')

class ProductCreateView(CreateView):
    model			= Product
    form_class      = ProductForm
    template_name	= 'product/create_product.html'
    success_url		= reverse_lazy('product:details')


class ProductUpdateView(UpdateView):
    model			= Product
    #form_class      = ProductForm
    fields			= "__all__"
    template_name	= 'product/product_update_form.html'
    template_name_suffix = '_update_form'
    success_url		= reverse_lazy('product:details')


class ProductDeleteView(DeleteView):
    model			= Product
    form_class      = ProductForm
    template_name	= 'product/product_confirm_delete.html'
    success_url		= reverse_lazy('product:details')
