from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Owner
from .forms import OwnerForm
# Create your views here.
class OwnerList(ListView):
    """ Owner ListView

    model: Owner

    template: owner_list.html

    Generates a listview of the Employees
    """
    model = Owner
    template_name = 'owner_list.html'

class OwnerCreate(CreateView):
    """ Owner CreateView

    model: Owner

    template: owner_create_form.html

    form: OwnerForm

    success_url: ownerlist, on success, redirect back to owner list

    Generates a standard createview for the Employee model
    """
    model = Owner
    template_name = 'owner_create_form.html'
    form_class = OwnerForm
    success_url = reverse_lazy('owner:ownerlist') # On success: redirect to list

class OwnerUpdate(UpdateView):
    """ Owner UpdateView

    model: Owner

    template: owner_update_form.html

    form: OwnerForm

    success_url: ownerlist, on success, redirect back to owner list

    Generates a standard updateview for the Employee model
    """
    model = Owner
    template_name = 'owner_update_form.html'
    form_class = OwnerForm
    success_url = reverse_lazy('owner:ownerlist') # On success: redirect to list

class OwnerDelete(DeleteView):
    """ Owner DeleteView

    model: Owner

    template: owner_delete_form.html

    success_url: ownerlist, on success, redirect back to owner list

    Generates a standard deleteview for the Employee model
    """
    model = Owner
    template_name = 'owner_delete_form.html'
    success_url = reverse_lazy('owner:ownerlist') # On success: redirect to list
