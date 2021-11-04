from django.forms import ModelForm, TextInput

from patient.models import Patient, Breed

class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = ['pet_name', 'animal_type', 'breed', 'age', 'owner']

class BreedForm(ModelForm):
    class Meta:
        model = Breed
        fields = ['animal', 'breed']
