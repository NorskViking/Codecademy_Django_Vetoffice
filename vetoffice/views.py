from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
"""
def home(request):
    template_name = 'templates/home.html'
    return render(request, 'templates/home.html')
"""
class home(TemplateView):
    template_name = 'home.html'
