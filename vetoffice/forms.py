from django.forms import ModelForm

from vetoffice.models import Owner, Patient, Appointment

class OwnerForm(ModelForm):
    class Meta:
        model = Owner
        fields = ['ownerID', 'first_name', 'last_name', 'phone']
