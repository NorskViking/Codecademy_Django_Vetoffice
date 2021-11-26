from django.urls import path
from . import views

app_name = 'employee'

""" Employee Url patterns

    creates a path for list, registration, editing and deletion of Employee instances.
"""
urlpatterns = [
    path('list/', views.EmployeeList.as_view(), name='employeelist'),
    path('register/', views.EmployeeCreate.as_view(), name='employeecreate'),
    path('<pk>/update/', views.EmployeeUpdate.as_view(), name='employeeupdate'),
    path('<pk>/delete/', views.EmployeeDelete.as_view(), name='employeedelete'),
]
