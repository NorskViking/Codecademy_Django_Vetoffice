from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.
class PatientList(ListView):
    model = Patient
    template_name = 'vetoffice/patient_list.html'

class PatientCreate(CreateView):
    model = Patient
    template_name = 'vetoffice/patient_create_form.html'
    form_class = PatientForm
    success_url = reverse_lazy('vetoffice:patientlist')

class PatientUpdate(UpdateView):
    model = Patient
    template_name = 'vetoffice/patient_update_form.html'
    form_class = PatientForm
    success_url = reverse_lazy('vetoffice:patientlist')

class PatientDelete(DeleteView):
    model = Patient
    template_name = 'vetoffice/patient_delete_form.html'
    success_url = reverse_lazy('vetoffice:patientlist')
