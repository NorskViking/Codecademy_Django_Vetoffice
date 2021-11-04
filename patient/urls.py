from django.urls import path
from . import views

urlpatterns = [
    #path('', views.home, name='home'),
    path('patient/list/', views.PatientList.as_view(), name='patientlist'),
    path('patient/register/', views.PatientCreate.as_view(), name='patientcreate'),
    path('patient/<pk>/update/', views.PatientUpdate.as_view(), name='patientupdate'),
    path('patient/<pk>/delete/', views.PatientDelete.as_view(), name='patientdelete'),
]
