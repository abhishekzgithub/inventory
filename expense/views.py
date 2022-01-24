from django.shortcuts import render
from django.views.generic import DetailView, CreateView, View, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from expense.models import Expense
from expense.forms import ExpenseForm
from django.conf import settings
from django.urls import reverse_lazy

class ExpenseView(LoginRequiredMixin, CreateView):
    login_url       = settings.LOGIN_URL
    model			= Expense
    form_class      = ExpenseForm
    template_name	= 'expense/expense.html'
    success_url		= reverse_lazy('expense:details')