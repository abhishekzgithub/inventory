from django.shortcuts import render
from order.models import Order
from product.models import Product
from expense.models import Expense
from django.contrib.auth.decorators import login_required
from django.conf import settings

@login_required(login_url=settings.LOGIN_URL)
def display_piechart(request, context={}):
    labels = ["January","February","March","April","May"]
    data = [65, 59, 80, 81, 56]

    # queryset = Order.objects.order_by('-created_timestamp')[:5]
    # for city in queryset:
    #     labels.append(city.name)
    #     data.append(city.population)

    # return render(request, 'pie_chart.html', {
    #     'labels': labels,
    #     'data': data,
    # })
    context["labels"]=labels
    context["data"]=data
    return render(request, "analytics/piechart.html", context)

@login_required(login_url=settings.LOGIN_URL)
def display_line_chart(request, context={}):
    labels = ["January","February","March","April","May"]
    data = [65, 59, 80, 81, 56, 55, 40]

    # queryset = Order.objects.order_by('-created_timestamp')[:5]
    # for city in queryset:
    #     labels.append(city.name)
    #     data.append(city.population)

    # return render(request, 'pie_chart.html', {
    #     'labels': labels,
    #     'data': data,
    # })
    context["labels"]=labels
    context["data"]=data
    return render(request, "analytics/linechart.html", context)

@login_required(login_url=settings.LOGIN_URL)
def display_bar_chart(request, context={}):
    labels = ["January","February","March","April","May"]
    data = [65, 59, 80, 81, 56, 55, 40]

    # queryset = Order.objects.order_by('-created_timestamp')[:5]
    # for city in queryset:
    #     labels.append(city.name)
    #     data.append(city.population)

    # return render(request, 'pie_chart.html', {
    #     'labels': labels,
    #     'data': data,
    # })
    context["labels"]=labels
    context["data"]=data
    return render(request, "analytics/barchart.html", context)

@login_required(login_url=settings.LOGIN_URL)
def display_order_status(request, status="created"):
    order_count = Order.objects.filter(status=status,ordered=True).count()
    return order_count

@login_required(login_url=settings.LOGIN_URL)
def display_all_orders(request):
    all_order = Order.objects.filter(ordered=True).all()
    return all_order


@login_required(login_url=settings.LOGIN_URL)
def display_all_expense(request):
    all_expense = Expense.objects.filter(user=request.user).all()
    return all_expense

@login_required(login_url=settings.LOGIN_URL)
def display_total_expense(request):
    total_expense = Expense.objects.filter(user=request.user).count()
    return total_expense