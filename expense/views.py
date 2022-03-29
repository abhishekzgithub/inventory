import imp
from django.shortcuts import redirect, render
from django.views.generic import DetailView, CreateView, View, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from expense.models import Expense
from expense.forms import ExpenseForm
from django.conf import settings
from django.urls import reverse_lazy
from account.models import User

class ExpenseView(LoginRequiredMixin, CreateView):
    login_url       = settings.LOGIN_URL
    model			= Expense
    form_class      = ExpenseForm
    template_name	= 'expense/expense.html'
    success_url		= reverse_lazy('expense:details')
    def post(self,request, context={}):
        form= ExpenseForm(request.POST or None)
        context["form"]=form
        if form.is_valid():
            expense=Expense.objects.create(
                user=User.objects.get(email=request.user.email),
                notes=form.cleaned_data.get("notes"),
                amount=form.cleaned_data.get("amount"),
            )
            expense.save()
            return redirect("expense:details")

        return render(request, "expense/expense.html", context)