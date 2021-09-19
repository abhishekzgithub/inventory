from django.shortcuts import render, redirect
from django.views.generic import FormView, DetailView, CreateView, View, UpdateView, DeleteView
from address.forms import AddressForm
from address.models import Address
from account.models import User
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings

class AddressCreateView(LoginRequiredMixin,CreateView):
    login_url       = settings.LOGIN_URL
    model			= Address
    fields			= "__all__"
    template_name	= 'address/address.html'
    success_url		= reverse_lazy('account:profile')


class AddressUpdateView(LoginRequiredMixin,UpdateView):
    login_url       = settings.LOGIN_URL
    model			= Address
    fields			= "__all__"
    template_name	= 'address/address.html'
    success_url		= reverse_lazy('account:profile')

class AddressDeleteView(LoginRequiredMixin,DeleteView):
    login_url       = settings.LOGIN_URL
    model			= Address
    template_name	= 'address/address_confirm_delete.html'
    success_url		= reverse_lazy('account:profile')
