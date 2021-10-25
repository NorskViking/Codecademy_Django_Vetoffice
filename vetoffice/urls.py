from django.urls import path
from django.contrib import admin

#from vetoffice.views import home, register_owner
from . import views

app_name = 'vetoffice'

urlpatterns = [
    path('', views.home, name='home'),
    path('register/owner', views.register_owner, name='register_owner'),
    path('owner/', views.owner, name='owner'),
    path('admin/', admin.site.urls),
]
