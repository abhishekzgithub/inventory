from django.shortcuts import render, redirect
from .models import Cart
# Create your views here.

def cart_view(request):
    context = {"message": "You have reached the Cart page."}
    cart_obj=Cart.objects.all()
    for cart in cart_obj:
        print(cart)
        prod = (cart.product.all())
        for item in prod:
            print(item)
            print("Title",item.title)
            print("Price",item.price)

    context["form"] = cart_obj
    #print(context["form"])
    return render(request, "cart/cart.html", context)