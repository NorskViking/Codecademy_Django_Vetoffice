from django.forms import ModelForm, TextInput

from vetoffice.models import Owner, Patient, Appointment, Breed

class OwnerForm(ModelForm):
    class Meta:
        model = Owner
        fields = ['first_name', 'last_name', 'phone']
        labels = {
            'first_name' : 'First name:',
            'last_name' : 'Family name:',
            'phone' : 'Phone'
        }

class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = ['pet_name', 'animal_type', 'breed', 'age', 'owner']

class BreedForm(ModelForm):
    class Meta:
        model = Breed
        fields = ['animal', 'breed']
