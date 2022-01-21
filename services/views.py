from django.shortcuts import render, redirect
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy, reverse
from account.models import User
from services.forms import ServicesForm
from services.models import Services
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings


@login_required(login_url=settings.LOGIN_URL)
def per_services_view(request,pk):
    context={"services":""}
    if request.method=="GET":
        context["services"] = Services.objects.filter(pk=pk).all()
    return render(request, "services/per_services_details.html", context)

class ServicesAllView(LoginRequiredMixin, View):
    login_url = settings.LOGIN_URL
    def get(self, request, context={}):
        context={"services":None}
        if request.user and (not request.user.is_anonymous) and (request.user.email) and (request.user.is_authenticated):
            context = {"message": "{} has reached the Services page.".format(request.user)}
            services_obj=Services.objects.all()#filter(user=User.objects.get(email=request.user.email))
            if services_obj:
                #services_obj=services_obj.all()
                context["services"]=services_obj
        return render(request, "services/services_details.html", context)

class ServicesDetailView(LoginRequiredMixin, DetailView):
    login_url       = settings.LOGIN_URL
    model			= Services
    fields			= "__all__"
    template_name	= 'services/services.html'
    success_url		= reverse_lazy('services:details')

class ServicesCreateView(LoginRequiredMixin, CreateView):
    login_url       = settings.LOGIN_URL
    model			= Services
    form_class      = ServicesForm
    template_name	= 'services/create_services.html'
    success_url		= reverse_lazy('services:details')


class ServicesUpdateView(LoginRequiredMixin, UpdateView):
    login_url       = settings.LOGIN_URL
    model			= Services
    #form_class      = ServicesForm
    fields			= "__all__"
    template_name	= 'services/services_update_form.html'
    template_name_suffix = '_update_form'
    success_url		= reverse_lazy('services:details')


class ServicesDeleteView(LoginRequiredMixin, DeleteView):
    login_url       = settings.LOGIN_URL
    model			= Services
    form_class      = ServicesForm
    template_name	= 'services/services_confirm_delete.html'
    success_url		= reverse_lazy('services:details')
