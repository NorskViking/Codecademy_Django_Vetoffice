from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Owner
from .forms import OwnerForm
# Create your views here.
class OwnerList(ListView):
    model = Owner
    template_name = 'owner_list.html'

class OwnerCreate(CreateView):
    model = Owner
    template_name = 'owner_create_form.html'
    form_class = OwnerForm
    success_url = reverse_lazy('owner:ownerlist')

class OwnerUpdate(UpdateView):
    model = Owner
    template_name = 'owner_update_form.html'
    form_class = OwnerForm
    success_url = reverse_lazy('owner:ownerlist')

class OwnerDelete(DeleteView):
    model = Owner
    template_name = 'owner_delete_form.html'
    success_url = reverse_lazy('owner:ownerlist')
