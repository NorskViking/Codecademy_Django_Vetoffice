from django.db import models
from owner.models import Owner

# Create your models here.
class Animal(models.Model):
    animal_type = models.CharField(max_length=200, default='Unkown')

    def __str__(self):
        return self.animal_type

    class Meta:
        ordering = ['animal_type']

class Breed(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    breed = models.CharField(max_length=200, default='Unknown')

    def __str__(self):
        return self.breed
    def __Str__(self):
        return self.animal

    def limit_breed_choices(animal):
        breed_in_animal = []
        for breed in self.animal:
            breed_in_animal.append(breed)
        return breed_in_animal

    class Meta:
        ordering = ['animal']

class Patient(models.Model):
	#The Patient table, with patientID as primary key
	#Owner is foreign key, as the paitent can only have one owner
	"""Create the patient SQLite Table.

	Stores a 'Patient' related to a Owner and one or more Appointments.

	Primary Key: patientID, used as Foreign Key for Appointment

	Foreign Key: owner = Owner:ownerID

	Fields: patientID(String), pet_name(string), animal_type(string), breed(string,)
	age(integer), owner(Foreign key, delete all on Owner removed)

	List: Animal_Type_Choices.

	__str__ for easy coupling pet_name and animal_type:breed of patient.
	"""
	pet_name = models.CharField(max_length=200)
	animal_type = models.ForeignKey(Animal, on_delete=models.CASCADE)
    breed = models.ForeignKey(Breed, limit_choices_to=limit_breed_choices, on_delete=models.CASCADE)
    age = models.IntegerField(default=0)
	owner = models.ForeignKey(Owner, on_delete=models.CASCADE)

	def __str__(self):
		#Returns pet name and animal_type
		return self.pet_name + ", " + self.animal_type

	class Meta:
		ordering = ["owner"]

    #breed = models.ForeignKey(Breed, limit_choices_to={Breed.animal == 'animal_type'}, on_delete=models.CASCADE)
    #breed = models.ForeignKey(Breed, limit_choices_to={Breed.animal == 'animal_type'}, on_delete=models.CASCADE)
