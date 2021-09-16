from django.shortcuts import render, redirect
from django.views.generic import FormView, DetailView, CreateView, View, UpdateView, DeleteView
from address.forms import AddressForm
from address.models import Address
from account.models import User
from django.urls import reverse_lazy

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



def delete_address(request, pk):
    user_email=request.user.email
    user_obj=User.objects.filter(email=user_email)
    if user_obj:
        address_obj= Address.objects.get(pk=pk)
        if address_obj:
            address_obj.delete()
    return redirect("/account/profile/")


class AddressUpdateView(UpdateView):
    model			= Address
    fields			= "__all__"
    template_name	= 'address/address.html'
    success_url		= reverse_lazy('account:profile')

class AddressDeleteView(DeleteView):
    model			= Address
    #fields			= "__all__"
    template_name	= 'address/address_confirm_delete.html'
    success_url		= reverse_lazy('account:profile')
