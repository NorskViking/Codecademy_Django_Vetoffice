from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.views.decorators.http import require_POST

from vetoffice.forms import OwnerForm
from vetoffice.models import Owner

# Create your views here.
def home(request):
    template_name = 'vetoffice/home.html'
    return render(request, 'vetoffice/home.html')

def owner(request):
    owner_list = Owner.objects.order_by('last_name')
    #owner = get_object_or_404(Owner)
    context = {'owner_list' : owner_list}
    return render(request, 'vetoffice/owner.html', context)
    #return render(request, 'vetoffice/owner.html')



#@require_POST
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
