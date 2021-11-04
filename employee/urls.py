from django.urls import path
from . import views

app_name = 'employee'

urlpatterns = [
    #path('', views.home, name='home'),
    path('list/', views.EmployeeList.as_view(), name='employeelist'),
    path('register/', views.EmployeeCreate.as_view(), name='employeecreate'),
    path('<pk>/update/', views.EmployeeUpdate.as_view(), name='employeeupdate'),
    path('<pk>/delete/', views.EmployeeDelete.as_view(), name='employeedelete'),
]
