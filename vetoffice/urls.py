from django.urls import path
#from django.contrib import admin
from . import views

from .views import home

app_name = 'vetoffice'

urlpatterns = [
<<<<<<< HEAD
    path('', views.home.as_view(), name='home'),
=======
    path('', views.home, name='home'),
    path('owner/list/', views.OwnerList.as_view(), name='ownerlist'),
    path('owner/register/', views.OwnerCreate.as_view(), name='ownercreate'),
    path('owner/<pk>/update/', views.OwnerUpdate.as_view(), name='ownerupdate'),
    path('owner/<pk>/delete/', views.OwnerDelete.as_view(), name='ownerdelete'),
    path('patient/list/', views.PatientList.as_view(), name='patientlist'),
    path('patient/register/', views.PatientCreate.as_view(), name='patientcreate'),
    path('patient/<pk>/update/', views.PatientUpdate.as_view(), name='patientupdate'),
    path('patient/<pk>/delete/', views.PatientDelete.as_view(), name='patientdelete'),
    path('breed/list/', views.BreedList.as_view(), name='breedlist'),
    path('breed/register/', views.BreedCreate.as_view(), name='breedcreate'),
    path('breed/<pk>/update/', views.BreedUpdate.as_view(), name='breedupdate'),
    path('breed/<pk>/delete/', views.BreedDelete.as_view(), name='breeddelete'),
    #path('admin/', admin.site.urls),
>>>>>>> master
]
