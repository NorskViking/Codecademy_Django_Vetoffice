from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from employee.models import Employee
from employee.forms import EmployeeForm
# Create your views here.

""" Employee List View

    Uses the django ListView to create a simple list of employee instances.

    Model: Employee from employee.models

    Template: employee_list.html
"""
class EmployeeList(ListView):
    model = Employee
    template_name = 'employee_list.html'

""" Employee Create View

    Uses the django CreateView and Form to create a simple formtable to create employee instances.

    Model: Employee from employee.models

    Template: employee_create_form.html

    Form: EmployeeForm from employee.forms

    Success_url: Employeelist

    Initial: gives an prompt for how the email for employee should look.
"""
class EmployeeCreate(CreateView):
    model = Employee
    template_name = 'employee_create_form.html'
    form_class = EmployeeForm
    success_url = reverse_lazy('employee:employeelist')
    initial = {'email': 'lastname@vetoffice.com'}

""" Employee Update View

    Uses the django UpdateView to create a simple form to edit employee instances.

    Model: Employee from employee.models

    Template: employee_update_form.html

    Form: EmployeeForm from employee.forms

    Success_url: Employeelist
"""
class EmployeeUpdate(UpdateView):
    model = Employee
    template_name = 'employee_update_form.html'
    form_class = EmployeeForm
    success_url = reverse_lazy('employee:employeelist')

""" Employee Delete View

    Uses the django DeleteView to create a simple form to delete employee instances.

    Model: Employee from employee.models

    Template: employee_delete_form.html

    Form: EmployeeForm from employee.forms

    Success_url: Employeelist
"""
class EmployeeDelete(DeleteView):
    model = Employee
    template_name = 'employee_delete_form.html'
    success_url = reverse_lazy('employee:employeelist')
