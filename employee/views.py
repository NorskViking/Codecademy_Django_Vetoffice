from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from employee.models import Employee
from employee.forms import EmployeeForm
# Create your views here.
class EmployeeList(ListView):
    model = Employee
    template_name = 'employee_list.html'

class EmployeeCreate(CreateView):
    model = Employee
    template_name = 'employee_create_form.html'
    form_class = EmployeeForm
    success_url = reverse_lazy('employee:employeelist')

class EmployeeUpdate(UpdateView):
    model = Employee
    template_name = 'employee_update_form.html'
    form_class = EmployeeForm
    success_url = reverse_lazy('employee:employeelist')

class EmployeeDelete(DeleteView):
    model = Employee
    template_name = 'employee_delete_form.html'
    success_url = reverse_lazy('employee:employeelist')
