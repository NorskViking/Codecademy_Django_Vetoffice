from django.urls import path
#from django.contrib import admin
from . import views

from .views import home, AppointmentCreate, AppointmentUpdate, AppointmentDelete

app_name = 'vetoffice'

urlpatterns = [
    path('', views.home.as_view(), name='home'),
    path('list/', views.AppointmentList.as_view(), name='appointmentlist'),
    path('register/', views.AppointmentCreate.as_view(), name='appointmentcreate'),
    path('<pk>/update/', views.AppointmentUpdate.as_view(), name='appointmentupdate'),
    path('<pk>/delete/', views.AppointmentDelete.as_view(), name='appointmentdelete'),
]
