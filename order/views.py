from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from order.forms import OrderForm, OrderItemForm
from order.models import Order, OrderItem
from account.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.views.generic import DetailView, CreateView, View, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

class OrderAllView(LoginRequiredMixin, DetailView):
    login_url = settings.LOGIN_URL
    model			= Order
    form_class      = OrderForm
    template_name	= 'order/order_details.html'
    success_url		= reverse_lazy('order:details')

class OrderItemAllView(LoginRequiredMixin, View):
    def get(self,request, context={}):
        if request.user and (not request.user.is_anonymous) and (request.user.email) and (request.user.is_authenticated):
            context={"orders":None}
            context = {"message": "{} has reached the Order page.".format(request.user)}
            order_item_obj=OrderItem.objects.filter(user=User.objects.get(email=request.user.email)).all()
            if order_item_obj:
                context["orders"]=order_item_obj
        return render(request, "order/order_details.html", context)


class OrderItemCreateView(LoginRequiredMixin, CreateView):
    login_url       = settings.LOGIN_URL
    model			= OrderItem
    form_class      = OrderItemForm
    template_name	= 'order/create_order.html'
    success_url		= reverse_lazy('order:details')

class OrderItemUpdateView(LoginRequiredMixin, UpdateView):
    login_url       = settings.LOGIN_URL
    model			= OrderItem
    form_class      = OrderItemForm
    template_name	= 'order/order_item_update_form.html'
    success_url		= reverse_lazy('order:details')


class OrderItemDeleteView(LoginRequiredMixin, DeleteView):
    login_url       = settings.LOGIN_URL
    model			= OrderItem
    form_class      = OrderItemForm
    template_name	= 'order/order_item_confirm_delete.html'
    success_url		= reverse_lazy('order:details')

@login_required(login_url=settings.LOGIN_URL)
def submit_form(request, context={}):
    if request.user and (not request.user.is_anonymous) and (request.user.email) and (request.user.is_authenticated):
        context={"form":None}
        context = {"message": "{} has reached the Order page.".format(request.user)}
        if request.method=="GET":
            form = OrderForm()
            user_obj=User.objects.get(email=request.user.email)
            form.fields["items"].queryset = OrderItem.objects.filter(user=user_obj).all() # 3 values so errors out
            context["form"]=form
        elif request.method=="POST":
            form = OrderForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("/order")
            else:
                print(form.errors)
    return render(request, "order/submit_order.html", context)