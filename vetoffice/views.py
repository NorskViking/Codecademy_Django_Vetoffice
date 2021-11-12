from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_requiered
from django.contrib.auth.mixins import LoginRequieredMixin
from django.contrib.auth.forms import UserCreationForm

from vetoffice.models import Appointment
from vetoffice.forms import AppointmentForm
# Create your views here.
"""
def home(request):
    template_name = 'templates/home.html'
    return render(request, 'templates/home.html')
"""
class home(TemplateView):
    template_name = 'home.html'

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class AppointmentList(LoginRequieredMixin, ListView):
    model = Appointment

class AppointmentCreate(LoginRequieredMixin, CreateView):
    model = Appointment
    template_name = 'appointment_create_form.html'
    form_class = AppointmentForm
    success_url = reverse_lazy('vetoffice:appointmentcreate')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return supert().form_valid(form)

class AppointmentUpdate(LoginRequieredMixin, UpdateView):
    model = Appointment
    template_name = 'appointment_create_form.html'
    form_class = AppointmentForm
    success_url = reverse_lazy('vetoffice:appointmentupdate')

class AppointmentDelete(LoginRequieredMixin, DeleteView):
    model = Appointment
    template_name = 'appointment_create_form.html'
    form_class = AppointmentForm
    success_url = reverse_lazy('vetoffice:appointmentdelete')
