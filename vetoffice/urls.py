from django.urls import path
#from django.contrib import admin
from vetoffice import views

app_name = 'vetoffice'

urlpatterns = [
    path('', views.home, name='home'),
]
