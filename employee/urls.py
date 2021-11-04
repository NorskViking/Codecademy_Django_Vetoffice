from django.urls import path
from . import views

app_name = 'employee'

urlpatterns = [
    #path('', views.home, name='home'),
    path('employee/list/', views.EmployeeList.as_view(), name='employeelist'),
    path('employee/register/', views.EmployeeCreate.as_view(), name='employeecreate'),
    path('employee/<pk>/update/', views.EmployeeUpdate.as_view(), name='employeeupdate'),
    path('employee/<pk>/delete/', views.EmployeeDelete.as_view(), name='employeedelete'),
]
