from django.shortcuts import render, redirect
from product.forms import ProductForm
from product.models import Product
from django.http import HttpResponseRedirect

def product_view(request):
    context = {"message": "You have reached the Product page."}
    context["form"]=Product.objects.all()
    return render(request, "product/product.html", context)

def per_product_view(request,id):
    context={"form":""}
    if request.method=="GET":
        context["form"] = Product.objects.get_by_id(id)
    return render(request, "product/product_details.html", context)
