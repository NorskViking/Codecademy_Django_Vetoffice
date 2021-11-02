from django.forms import ModelForm, TextInput

from vetoffice.models import Owner, Patient, Appointment

class OwnerForm(ModelForm):
    class Meta:
        model = Owner
        fields = ['first_name', 'last_name', 'phone']
        labels = {
            'first_name' : 'First Name:',
            'last_name' : 'Family name:',
            'phone' : 'Phone'
        }

class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = ['pet_name', 'animal_type', 'breed', 'age', 'owner']
