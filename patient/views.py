from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from patient.models import Animal, Breed, Patient
from patient.forms import AnimalForm, BreedForm, PatientForm
# Create your views here.
class BreedList(ListView):
    model = Animal
    template_name = 'patient/animal_list.html'

class AnimalCreate(CreateView):
    model = Animal
    template_name = 'patient/animal_create_form.html'
    form_class = AnimalForm
    success_url = reverse_lazy('patient:animallist')

class AnimalUpdate(UpdateView):
    model = Animal
    template_name = 'patient/animal_update_form.html'
    form_class = AnimalForm
    success_url = reverse_lazy('patient:animallist')

class AnimalDelete(DeleteView):
    model = Animal
    template_name = 'patient/animal_delete_form.html'
    success_url = reverse_lazy('patient:animallist')

class BreedList(ListView):
    model = Breed
    template_name = 'patient/breed_list.html'

class BreedCreate(CreateView):
    model = Breed
    template_name = 'patient/breed_create_form.html'
    form_class = BreedForm
    success_url = reverse_lazy('patient:breedlist')

class BreedUpdate(UpdateView):
    model = Breed
    template_name = 'patient/breed_update_form.html'
    form_class = BreedForm
    success_url = reverse_lazy('patient:breedlist')

class BreedDelete(DeleteView):
    model = Breed
    template_name = 'patient/breed_delete_form.html'
    success_url = reverse_lazy('patient:breedlist')

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
