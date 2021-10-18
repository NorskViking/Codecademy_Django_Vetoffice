from django.shortcuts import render

pets = [
{'petname': 'Fido', 'animal_type': 'Dog'},
]
# Create your views here.
def home(request):
    context = {"name": "<Put your name here>", "pets": pets}
    return render(request, 'vetoffice/home.html', context)
