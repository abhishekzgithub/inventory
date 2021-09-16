from django.shortcuts import render, redirect
from django.views.generic import FormView, DetailView, CreateView, View, UpdateView, DeleteView
from address.forms import AddressForm
from address.models import Address
from account.models import User
from django.urls import reverse_lazy

class AddressCreateView(CreateView):
    model			= Address
    fields			= "__all__"
    template_name	= 'address/address.html'
    success_url		= reverse_lazy('account:profile')


class AddressUpdateView(UpdateView):
    model			= Address
    fields			= "__all__"
    template_name	= 'address/address.html'
    success_url		= reverse_lazy('account:profile')

class AddressDeleteView(DeleteView):
    model			= Address
    template_name	= 'address/address_confirm_delete.html'
    success_url		= reverse_lazy('account:profile')
