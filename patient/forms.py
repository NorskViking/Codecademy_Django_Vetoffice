from django.forms import ModelForm, TextInput

from patient.models import Animal, Breed, Patient

class AnimalTypeForm(ModelForm):
    class Meta:
        model = AnimalType
        fields = ['animal_type']

class BreedForm(ModelForm):
    class Meta:
        model = Breed
        fields = ['animal', 'breed']

class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = ['pet_name', 'animal_type', 'breed', 'age', 'owner']
