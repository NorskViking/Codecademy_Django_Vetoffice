from django.contrib import admin

from .models import Employee
# Register your models here.
admin.site.register(Employee) # Allows for registration of employees in the admin page.
