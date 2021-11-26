from django.forms import ModelForm, TextInput

from employee.models import Employee

""" Employee modelForm
    Uses the Django form to create an html/css form for creating and editing an employee instance.

    Model: Employee from employee.models

    fields: title, first_name, last_name, phone, email
"""
class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['title', 'first_name', 'last_name', 'phone', 'email']
