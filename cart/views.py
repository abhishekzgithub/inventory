from django.shortcuts import render, redirect
from .models import Cart
# Create your views here.

def cart_view(request):
    context = {"message": "You have reached the Cart page."}
    cart_obj=Cart.objects.all()
    context["form"] = cart_obj
    return render(request, "cart/cart.html", context)

def cart_update(request):
    """
    get the product id and check if the method is add or delete
    if the method is add, then check for the product id and add it into cart class
    if method is delete, then delete the product from the cart class
    """
    print(request.POST)
    product_id = request.POST.get('product_id')
    context={}
    Cart().save()
    return render(request, "cart/cart.html", context)
