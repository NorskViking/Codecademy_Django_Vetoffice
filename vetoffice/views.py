from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from vetoffice.forms import OwnerForm, PatientForm
from vetoffice.models import Owner, Patient

# Create your views here.
def home(request):
    template_name = 'vetoffice/home.html'
    return render(request, 'vetoffice/home.html')

class OwnerList(ListView):
    model = Owner
    template_name = 'vetoffice/owner_list.html'

class OwnerCreate(CreateView):
    model = Owner
    template_name = 'vetoffice/owner_create_form.html'
    form_class = OwnerForm
    #fields = ['last_name', 'first_name', 'phone']

class OwnerUpdate(UpdateView):
    model = Owner
    template_name = 'vetoffice/owner_update_form.html'
    form_class = OwnerForm
    #fields = ['last_name', 'first_name', 'phone']

class OwnerDelete(DeleteView):
    model = Owner
    template_name = 'vetoffice/owner_delete_form.html'
    success_url = '/owner/list/'
    fields = []

class PatientList(ListView):
    model = Patient
    template_name = 'vetoffice/patient_list.html'

class PatientCreate(CreateView):
    model = Patient
    template_name = 'vetoffice/patient_create_form.html'
    form_class = PatientForm
    #fields = ['pet_name', 'animal_type', 'breed', 'age', 'owner']

class PatientUpdate(UpdateView):
    model = Patient
    template_name = 'vetoffice/patient_update_form.html'
    form_class = PatientForm
    #fields = ['pet_name', 'animal_type', 'breed', 'age', 'owner']

class PatientDelete(DeleteView):
    model = Patient
    template_name = 'vetoffice/patient_delete_form.html'
    success_url = '/patient/list/'
    #fields = []
