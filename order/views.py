from dataclasses import fields
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from order.forms import OrderForm, OrderItemForm
from order.models import Order, OrderItem
from product.models import Product
from account.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.views.generic import DetailView, CreateView, View, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.views.generic.edit import DeleteView
from django.core.exceptions import ObjectDoesNotExist

# class OrderAllView(LoginRequiredMixin, DetailView):
#     login_url = settings.LOGIN_URL
#     model			= Order
#     form_class      = OrderForm
#     template_name	= 'order/order_details.html'
#     success_url		= reverse_lazy('order:details')

class OrderView(LoginRequiredMixin, View):
    def get(self,request, context={}):
        try:
            if request.user and (not request.user.is_anonymous) and (request.user.email) and (request.user.is_authenticated):
                context["orders"]=None
                context["message"] = "{} has reached the Order page.".format(request.user)
                order_item_obj=Order.objects.get(user=User.objects.get(email=request.user.email),
                                                    ordered=False)
                if order_item_obj:
                    context["orders"]=order_item_obj
        except ObjectDoesNotExist:
                print("No Order created yet.")
        return render(request, "order/order_details.html", context)
    
    def post(self, request, pk, context={}):
        product = Product.objects.get(id=pk)
        order_item, created = OrderItem.objects.get_or_create(
            product=product,
            user=request.user,
            ordered=False
        )
        order_qs = Order.objects.filter(user=request.user
                                        #, ordered=False
                                        )
        if order_qs.exists():
            order = order_qs[0]
            # check if the order item is in the order
            if order_item in order.items.all():#order.items.filter(id=product.id).exists():
                order_item.quantity += 1
                order_item.save()
                #messages.info(request, "This item quantity was updated.")
                return redirect("order:details")
            else:
                order.items.add(order_item)
                #messages.info(request, "This item was added to your cart.")
                return redirect("order:details")
        else:
            ordered_date = timezone.now()
            order = Order.objects.create(
                                    user=request.user, 
                                    ordered_date=ordered_date,
                                    ordered=False)
            order.items.add(order_item)
            order.save()
            #messages.info(request, "This item was added to your cart.")
            return redirect("order:details")

class OrderSubmitView(LoginRequiredMixin, View):
    # login_url       = settings.LOGIN_URL
    # model			= Order
    # form_class      = OrderForm
    # template_name	= 'order/submit_order.html'
    # success_url		= reverse_lazy('order:details')

    def post(self,request,pk, context={}):
        return render(request, "order/order_details.html", context)

class OrderItemUpdateView(LoginRequiredMixin, UpdateView):
    login_url       = settings.LOGIN_URL
    model			= OrderItem
    fields          = ["quantity"]
    template_name	= 'order/order_item/order_item_update_form.html'
    success_url		= reverse_lazy('order:details')

class OrderItemDeleteView(LoginRequiredMixin, DeleteView):
    login_url       = settings.LOGIN_URL
    model			= OrderItem
    fields          = '__all__'
    template_name	= 'order/order_item/order_item_confirm_delete.html'
    success_url		= reverse_lazy('order:details')
