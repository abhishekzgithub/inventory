from django.shortcuts import render, redirect
from order.forms import OrderForm
from order.models import Order
from account.models import User
from cart.models import Cart
from address.models import Address
from django.forms.models import model_to_dict
from django.http import HttpResponseRedirect


def order_view(request):
    context = {"message": "You have reached the order_view page."}
    user_email=request.user.email
    form=OrderForm()
    try:
        if user_email:
            user_obj=User.objects.get(email=user_email)
            cart_obj=Cart.objects.filter(user=user_obj)
            if cart_obj and user_obj:
                cart_obj=cart_obj.latest('updated_timestamp')
                order_obj=Order.objects.filter(user=user_obj,cart=cart_obj)
                if order_obj:
                    order_obj=order_obj.latest('updated_timestamp')
                    form=OrderForm(
                    initial=model_to_dict(order_obj)
                    )
    except Exception as exc:
        print(exc)
    context["form"]=form
    return render(request, "order/submit_order.html", context)

def create_order(request):
    context = {"message": "You have reached the create_order page."}
    user_email=request.user.email
    form=OrderForm()
    try:
        if user_email:
            user_obj=User.objects.get(email=user_email)
            cart_obj=Cart.objects.filter(user=user_obj)
            if cart_obj and user_obj:
                cart_obj=cart_obj.latest('updated_timestamp')
                form.fields["user"].queryset = User.objects.filter(email=user_email)
                form.fields["cart"].queryset = Cart.objects.filter(user=user_obj)
                form.fields["delivery_address"].queryset = Address.objects.filter(user=user_obj)

    except Exception as exc:
        print(exc)
    context["form"]=form
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/order")
    return render(request, "order/submit_order.html", context)

