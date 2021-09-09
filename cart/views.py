from django.shortcuts import render, redirect
from .models import Cart
from account.models import User
from product.models import Product
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
    user_email=request.user.email
    product_id = request.POST.get('product_id')
    context={}
    cart_obj=Cart.objects.get_or_create(user=User.objects.get(email=user_email))[0]
    cart_obj.product.add(Product.objects.get(id=product_id))
    cart_obj.save()
    return render(request, "cart/cart.html", context)

def cart_delete(request):
    print(request.POST)
    user_email=request.user.email
    product_id = request.POST.get('product_id')
    context={}
    cart_obj=Cart.objects.get_or_create(user=User.objects.get(email=user_email))[0]
    cart_obj.product.remove(Product.objects.get(id=product_id))
    cart_obj.save()
    return render(request, "cart/cart.html", context)