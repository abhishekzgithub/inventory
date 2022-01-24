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
                                        , ordered=False
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

class OrderSubmitView(LoginRequiredMixin, CreateView):
    login_url       = settings.LOGIN_URL
    model			= Order
    form_class      = OrderForm
    template_name	= 'order/submit_order.html'
    success_url		= reverse_lazy('order:details')

    def post(self,request,pk, context={}):
        form = OrderForm(request.POST)
        if form.is_valid():
            delivery_address=form.cleaned_data.get("delivery_address")
            payment_method=form.cleaned_data.get("payment_method")
            status = form.cleaned_data.get("status")
            notes = form.cleaned_data.get("notes")
            ordered_date=form.cleaned_data.get("ordered_date")
            delivery_date=form.cleaned_data.get("delivery_date")
            order_obj = Order.objects.get(id=pk)
            order_obj.delivery_address=delivery_address
            order_obj.ordered=True
            order_obj.status=status
            order_obj.payment_method=payment_method
            #order_obj.delivery_charge=delivery_charge
            #order_obj.discount=discount
            order_obj.total=order_obj.get_total()
            order_obj.notes=notes
            order_obj.ordered_date=ordered_date
            order_obj.delivery_date=delivery_date
            order_obj.save()
            order_item = OrderItem.objects.filter(ordered=False).update(ordered=True)
        else:
            print(form.errors)
            print(form.error_messages)
        return redirect("product:details")

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


@login_required(login_url=settings.LOGIN_URL)
def apply_discount_to_order(request, pk):
    if request.POST:
        if request.POST.get("reset_discount_percent",None):
            discount_percent=float(request.POST["reset_discount_percent"])
        elif request.POST.get("discount_percent", None):
            discount_percent=float(request.POST["discount_percent"])
        if discount_percent<0 or discount_percent>100:
            return redirect("order:details") 
        order=Order.objects.get(id=pk)
        if order.discount>0.00:
            discount_percent=(discount_percent+float(order.discount))-order.discount
        order.discount=discount_percent
        order.save()
    return redirect("order:details")