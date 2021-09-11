from django.shortcuts import render, redirect
from order.forms import OrderForm
from order.models import Order
from account.models import User
from cart.models import Cart
from django.forms.models import model_to_dict

from django.http import HttpResponseRedirect


def order_view(request):
    context = {"message": "You have reached the order_view page."}
    user_email=request.user.email
    user_obj=User.objects.get(email=user_email)
    cart_obj=Cart.objects.filter(user=user_obj).latest('updated_timestamp')
    order_obj=Order.objects.filter(user=user_obj,cart=cart_obj).latest('updated_timestamp')
    form=OrderForm(
        initial=model_to_dict(order_obj)
        # {
        #     'user': User.objects.get(email=user_email),
        #     'cart': Cart.objects.filter(user=user_obj).latest('updated_timestamp'),

        # }
    )
    context["form"]=form
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            #form.save()
            return HttpResponseRedirect("/order")
    return render(request, "order/create_order.html", context)


