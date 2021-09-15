from django.shortcuts import render, redirect
from cart.models import Cart
from account.models import User
from product.models import Product
from django.http import HttpResponseRedirect

def cart_view(request):
    user=request.user
    context = {"message": "{} has reached the Cart page.".format(user)}
    context["cart"]=None
    if user and not user.is_anonymous:
        user_email=user.email
        cart_obj=Cart.objects.filter(user=User.objects.get(email=user_email))
        if cart_obj:
            cart_obj=cart_obj.latest('updated_timestamp')
        context["cart"] = cart_obj
    return render(request, "cart/cart.html", context)

def cart_update(request):
    """
    get the product id and check if the method is add or delete
    if the method is add, then check for the product id and add it into cart class
    if method is delete, then delete the product from the cart class
    """
    user=request.user
    if user and not user.is_anonymous:
        user_email=user.email
        product_id = request.POST.get('product_id')
        try:
            if user_email:
                cart_obj=Cart.objects.filter(user=User.objects.get(email=user_email))
                if cart_obj:
                    cart_obj=cart_obj.latest("updated_timestamp")
                else:
                    cart_obj=Cart.objects.get_or_create(user=User.objects.get(email=user_email))
                    cart_obj=cart_obj[0]
                cart_obj.product.add(Product.objects.get(id=product_id))
                cart_obj.save()
        except Exception as exc:
            print(exc)
    return HttpResponseRedirect("/product")

def cart_delete(request):
    user=request.user
    if user and not user.is_anonymous:
        user_email=user.email
        product_id = request.POST.get('product_id', None)
        try:
            if user_email and product_id:
                cart_obj=Cart.objects.filter(user=User.objects.get(email=user_email))
                if cart_obj:
                    cart_obj=cart_obj.latest("updated_timestamp")       
                    cart_obj.product.remove(Product.objects.get(id=product_id))
                    cart_obj.save()
            else:
                raise Exception
        except Exception as exc:
            print(exc)
    return HttpResponseRedirect("/product")