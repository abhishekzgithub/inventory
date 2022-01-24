from django.conf.urls import url, include
import expense.views as expense_views

urlpatterns = [
    
    url("^$", expense_views.ExpenseView.as_view(), name="details"),
   

]