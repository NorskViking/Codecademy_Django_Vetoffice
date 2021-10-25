from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from vetoffice.forms import OwnerForm
from vetoffice.models import Owner

# Create your views here.
def home(request):
    template_name = 'vetoffice/home.html'
    return render(request, 'vetoffice/home.html')

class owner_list(ListView):
    model = Owner
    template_name = 'vetoffice/owner.html'


def register_owner(request):
    #model = Owner
    #template_name = 'vetoffice/register_owner.html'
    if request.method == "POST":
        form = OwnerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vetoffice:home')
    else:
        form = OwnerForm()
    return render(request, 'vetoffice/register_owner.html', {'form' : form})

    #return HttpResponse("Something went wrong.")
