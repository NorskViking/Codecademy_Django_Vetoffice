from django.forms import ModelForm, TextInput

from employee.models import Employee

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['title', 'first_name', 'last_name', 'phone']
