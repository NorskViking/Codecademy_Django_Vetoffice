from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

<<<<<<< HEAD
=======
from vetoffice.forms import OwnerForm, PatientForm, BreedForm
from vetoffice.models import Owner, Patient, Breed

>>>>>>> master
# Create your views here.
"""
def home(request):
<<<<<<< HEAD
    template_name = 'templates/home.html'
    return render(request, 'templates/home.html')
"""
class home(TemplateView):
    template_name = 'home.html'
=======
    template_name = 'vetoffice/home.html'
    return render(request, 'vetoffice/home.html')

class OwnerList(ListView):
    model = Owner
    template_name = 'vetoffice/owner_list.html'

class OwnerCreate(CreateView):
    model = Owner
    template_name = 'vetoffice/owner_create_form.html'
    form_class = OwnerForm
    success_url = reverse_lazy('vetoffice:ownerlist')

class OwnerUpdate(UpdateView):
    model = Owner
    template_name = 'vetoffice/owner_update_form.html'
    form_class = OwnerForm
    success_url = reverse_lazy('vetoffice:ownerlist')

class OwnerDelete(DeleteView):
    model = Owner
    template_name = 'vetoffice/owner_delete_form.html'
    success_url = reverse_lazy('vetoffice:ownerlist')

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

class BreedList(ListView):
    model = Breed
    template_name = 'vetoffice/breed_list.html'

class BreedCreate(CreateView):
    model = Breed
    template_name = 'vetoffice/breed_create_form.html'
    form_class = BreedForm
    success_url = reverse_lazy('vetoffice:breedlist')

class BreedUpdate(UpdateView):
    model = Breed
    template_name = 'vetoffice/breed_update_form.html'
    form_class = BreedForm
    success_url = reverse_lazy('vetoffice:breedlist')

class BreedDelete(DeleteView):
    model = Breed
    template_name = 'vetoffice/breed_delete_form.html'
    success_url = reverse_lazy('vetoffice:breedlist')
>>>>>>> master
