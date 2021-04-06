from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product
# Create your views here.
def product_view(request):
    context = {"message": "You have reached the Product page."}
    context["form"]=Product.objects.all()
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            # email = form.cleaned_data.get("email")
            # password = form.cleaned_data.get("password")
            return redirect("home")
    return render(request, "product/product.html", context)

def per_product_view(request,id):
    context={"form":""}
    context["form"] = Product.objects.get_by_id(id)
    return render(request, "product/product_details.html", context)
