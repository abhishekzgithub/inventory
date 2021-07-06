from django.shortcuts import render, redirect
from .models import Cart
# Create your views here.

def cart_view(request):
    context = {"message": "You have reached the Cart page."}
    cart_obj=Cart.objects.all()
    context["form"] = cart_obj
    return render(request, "cart/cart.html", context)

def cart_update(request):
    print(request.POST)
    product_id = request.POST.product_id
    context={}
    return render(request, "cart/cart.html", context)
