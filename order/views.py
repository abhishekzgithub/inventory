from django.shortcuts import render, redirect

# Create your views here.
def get_orders(request):
    context={"message":"You have reached the order page."}
    return render(request, "order/order_details.html", context)
