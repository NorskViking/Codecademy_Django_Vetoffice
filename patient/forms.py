from django.forms import ModelForm, TextInput

from patient.models import Animal, Breed, Patient

class AnimalForm(ModelForm):
    class Meta:
        model = Animal
        fields = ['animal_type']

class BreedForm(ModelForm):
    class Meta:
        model = Breed
        fields = ['animal', 'breed']

class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = ['pet_name', 'animal', 'breed', 'age', 'owner']
