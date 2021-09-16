from django.shortcuts import render, redirect
from django.views.generic import FormView, DetailView, CreateView, View
from address.forms import AddressForm
from address.models import Address
from account.models import User

class AddressCreateView(View):
    def get(self, request):
        context={}
        form=AddressForm()
        context["form"]=form
        return render(request, "address/address.html", context)

    def post(self, request):
        context={}
        username = request.user.username
        form=AddressForm(request.POST)
        if form.is_valid():
            form.save()
            # user_obj=User.objects.filter(username=username)
            # user_obj.update(address=form)
            # user_obj.save()
            return redirect("/address")
        else:
            print(form.errors)
            context["errors"]=form.errors
            form=AddressForm()
            context["form"]=form
        return render(request, "address/address.html", context)

    # template_name="address/address.html"
    # form_class= AddressForm
    # success_url = "/account/profile" #'workouts:exercise_detail'

    # def form_valid(self, form):
    #     #form.save()
    #     print(form)
    #     user=form.user
    #     user_obj=User.objects.get(email=form.user.email)
    #     user_obj.add(address=form)
    #     return super(AddressCreateView, self).form_valid(form)

class AddressDetails(DetailView):
    template_name="address/address.html"
    form_class= AddressForm
    model = Address
    success_url = "/account/profile"
    
    def get_context_data(self, **kwargs):
        context = super(AddressDetails, self).get_context_data(**kwargs)
        context['form'] = AddressForm
        return context
    

def create_address(request):
    pass

def delete_address(request):
    pass

def update_address(request):
    pass