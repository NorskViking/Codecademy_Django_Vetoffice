from django.urls import path
#from django.contrib import admin
from . import views

from .views import home, AppointmentList, AppointmentCreate, AppointmentUpdate, AppointmentDelete

app_name = 'vetoffice'

urlpatterns = [
    path('', views.home, name='home'),
    path('appointment/list/', views.AppointmentList.as_view(), name='appointmentlist'),
    path('appointment/register/', views.AppointmentCreate.as_view(), name='appointmentcreate'),
    path('appointment/<pk>/update/', views.AppointmentUpdate.as_view(), name='appointmentupdate'),
    path('appointment/<pk>/delete/', views.AppointmentDelete.as_view(), name='appointmentdelete'),
]
