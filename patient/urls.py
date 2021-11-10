from django.urls import path
from . import views

from .views import(
        Patient,
        PatientCreate,
        PatientUpdate,
        PatientDelete,
        )

app_name = 'patient'

urlpatterns = [
    #path('', views.home, name='home'),
    path('animal/list/', views.AnimalList.as_view(), name='animallist'),
    path('animal/register/', views.AnimalCreate.as_view(), name='animalcreate'),
    path('animal/<pk>/update/', views.AnimalUpdate.as_view(), name='animalupdate'),
    path('animal/<pk>/delete/', views.AnimalDelete.as_view(), name='animaldelete'),
    path('breed/list/', views.BreedList.as_view(), name='breedlist'),
    path('breed/register/', views.BreedCreate.as_view(), name='breedcreate'),
    path('breed/<pk>/update/', views.BreedUpdate.as_view(), name='breedupdate'),
    path('breed/<pk>/delete/', views.BreedDelete.as_view(), name='breeddelete'),
    path('list/', views.PatientList.as_view(), name='patientlist'),
    path('register/', views.PatientCreate.as_view(), name='patientcreate'),
    path('<pk>/update/', views.PatientUpdate.as_view(), name='patientupdate'),
    path('<pk>/delete/', views.PatientDelete.as_view(), name='patientdelete'),
]
