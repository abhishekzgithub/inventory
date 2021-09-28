from django.shortcuts import render, redirect
from order.forms import OrderForm
from order.models import Order
from account.models import User
from cart.models import Cart
from address.models import Address
from django.forms.models import model_to_dict
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.views.generic import FormView, DetailView, CreateView, View, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

@login_required(login_url=settings.LOGIN_URL)
def order_view(request):
    user=request.user
    context = {"message": "{} has reached the order_view page.".format(user)}
    form=None
    if user and not user.is_anonymous:
        user_email=user.email
        try:
            if user_email:
                user_obj=User.objects.get(email=user_email)
                cart_obj=Cart.objects.filter(user=user_obj)
                if cart_obj and user_obj:
                    cart_obj=cart_obj.latest('updated_timestamp')
                    order_obj=Order.objects.filter(user=user_obj,cart=cart_obj)
                    if order_obj:
                        order_obj=order_obj.latest('updated_timestamp')
                        form=OrderForm()
                        form.fields["user"].initial = User.objects.get(email=user_email)
                        form.fields["cart"].queryset = Cart.objects.filter(user=user_obj)
                        form.fields["delivery_address"].initial = order_obj.delivery_address
                        form.fields["shipping_cost"].initial = order_obj.shipping_cost
                        form.fields["total"].initial = order_obj.total

        except Exception as exc:
            print(exc)
    context["form"]=form
    return render(request, "order/order_details.html", context)

@login_required(login_url=settings.LOGIN_URL)
def create_order(request):
    user=request.user
    context = {"message": "{} has reached the create_order page.".format(user)}
    form=None
    if user and not user.is_anonymous:
        user_email=user.email
        try:
            if user_email:
                if request.method == "POST":
                    form = OrderForm(request.POST)
                    if form.is_valid():
                        form.save()
                        return redirect("/order")
                    else:
                        print(form.errors)
                else:
                    user_obj=User.objects.get(email=user_email)
                    cart_obj=Cart.objects.filter(user=user_obj)
                    address_obj = Address.objects.filter(user=user_obj)
                    if cart_obj and user_obj:
                        form=OrderForm()
                        cart_obj=cart_obj.latest('updated_timestamp')
                        form.fields["user"].queryset = User.objects.filter(email=user_email)
                        form.fields["cart"].queryset = Cart.objects.filter(user=user_obj)
                        form.fields["shipping_cost"].initial = 29
                        form.fields["total"].initial = cart_obj.cart_total+29
        except Exception as exc:
            print(exc)
        context["form"]=form
    return render(request, "order/create_order.html", context)

