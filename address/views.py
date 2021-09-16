from django.shortcuts import render, redirect
from django.views.generic import FormView, DetailView, CreateView, View
from address.forms import AddressForm
from address.models import Address
from account.models import User

class AddressCreateView(View):
    def get(self, request, context={}):
        form=AddressForm()
        context["form"]=form
        return render(request, "address/address.html", context)

    def post(self, request, context={}):
        username = request.user.username
        form=AddressForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/account/profile/")
        else:
            context["errors"]=form.errors
            return self.get(request, context)



def delete_address(request, id):
    user_email=request.user.email
    user_obj=User.objects.filter(email=user_email)
    if user_obj:
        address_obj= Address.objects.get(pk=id)
        if address_obj:
            address_obj.delete()
    return redirect("/account/profile/")

def update_address(request):
    pass