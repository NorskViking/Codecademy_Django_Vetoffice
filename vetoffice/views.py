from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm

from vetoffice.models import Appointment
from vetoffice.forms import AppointmentForm
# Create your views here.

@login_required
def home(request):
    context = {"name": request.user}
    return render(request, 'home.html', context)
"""
class home(TemplateView):
    template_name = 'home.html'
"""
class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class AppointmentList(LoginRequiredMixin, ListView):
    model = Appointment
    template_name = 'appointment_list.html'

class AppointmentCreate(LoginRequiredMixin, CreateView):
    model = Appointment
    template_name = 'appointment_create_form.html'
    form_class = AppointmentForm
    success_url = reverse_lazy('vetoffice:appointmentcreate')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class AppointmentUpdate(LoginRequiredMixin, UpdateView):
    model = Appointment
    template_name = 'appointment_create_form.html'
    form_class = AppointmentForm
    success_url = reverse_lazy('vetoffice:appointmentupdate')

class AppointmentDelete(LoginRequiredMixin, DeleteView):
    model = Appointment
    template_name = 'appointment_create_form.html'
    form_class = AppointmentForm
    success_url = reverse_lazy('vetoffice:appointmentdelete')
