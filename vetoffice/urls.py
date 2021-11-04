from django.urls import path
#from django.contrib import admin
from . import views

from .views import home

app_name = 'vetoffice'

urlpatterns = [
    path('', views.home.as_view(), name='home'),
]
