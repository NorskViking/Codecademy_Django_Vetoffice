from django.db import models
from owner.models import Owner

# Create your models here.
class Breed(models.Model):
    Animal_Type_Choices = [
		('Dog', 'Dog'),
		('Cat', 'Cat'),
		('Bird', 'Bird'),
		('Reptile', 'Reptile'),
		('Rabbit', 'Rabbit'),
		('Fish', 'Fish'),
		('Unknown', 'Unkown'),
	]

    animal = models.CharField(max_length=50, choices=Animal_Type_Choices, default='Unknown')
    breed = models.CharField(max_length=200, default='Unknown')


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
	Animal_Type_Choices = [
		('Dog', 'Dog'),
		('Cat', 'Cat'),
		('Bird', 'Bird'),
		('Reptile', 'Reptile'),
		('Rabbit', 'Rabbit'),
		('Fish', 'Fish'),
		('Unknown', 'Unkown'),
	]

	pet_name = models.CharField(max_length=200)
	animal_type = models.CharField(max_length=50, choices=Animal_Type_Choices, default='Unkown')
	breed = models.CharField(max_length=200, default='Unkown')
	age = models.IntegerField(default=0)
	owner = models.ForeignKey(Owner, on_delete=models.CASCADE)

	def __str__(self):
		#Returns pet name and animal_type
		return self.pet_name + ", " + self.animal_type

	class Meta:
		ordering = ["owner"]
