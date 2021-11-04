from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from patient.models import Patient
from patient.forms import PatientForm
# Create your views here.
class PatientList(ListView):
    model = Patient
    template_name = 'patient/patient_list.html'

class PatientCreate(CreateView):
    model = Patient
    template_name = 'patient/patient_create_form.html'
    form_class = PatientForm
    success_url = reverse_lazy('patient:patientlist')

class PatientUpdate(UpdateView):
    model = Patient
    template_name = 'patient/patient_update_form.html'
    form_class = PatientForm
    success_url = reverse_lazy('patient:patientlist')

class PatientDelete(DeleteView):
    model = Patient
    template_name = 'patient/patient_delete_form.html'
    success_url = reverse_lazy('patient:patientlist')
