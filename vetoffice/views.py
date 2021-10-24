from django.shortcuts import get_object_or_404, render, redirect

from vetoffice.forms import OwnerForm
from vetoffice.models import Owner

pets = [
{'petname': 'Fido', 'animal_type': 'Dog'},
]
# Create your views here.
def home(request):
    context = {"name": "<Put your name here>", "pets": pets}
    return render(request, 'vetoffice/home.html', context)


def register_owner(request):
    if request.method == "POST":
        form = OwnerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vetoffice:home')
        else:
            form = OwnerForm()
        return render(request, 'vetoffice/register_owner.html', {'form' : form})
