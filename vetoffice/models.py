from django.db import models
#TODO: Create Docstring comments for classes and functions

# Create your models here.
class Owner(models.Model):
	#The Owner table, with OwnerID as primary key
	#Owner can own several pets
	"""Create the Owner SQLite Table.

	Primary Key: OwnerID, used as Foreign Key for paitient

	Fields: first_name(String), last_name(string), phone(string(of numbers))

	__str__ for easy coupling first and last name of owner.

	Function: has_multiple_pets
				reurns boolean True if owner have several pets registered with the Vet Office.
	"""
	#id = models.BigAutoField(primary_key=True)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	phone = models.CharField(max_length=30)
	def __str__(self):
		#Returns the first and last name of owner with whitespace between
		return self.first_name + " " + self.last_name

	def has_multiple_pets(self):
		'''Do Owner have multiple pets.

		Checks if a owner have multiple pets registered at the vet Vetoffice
		and returns a boolean.

		parameters: self

		returns: boolean (True if owned pets are greater then 1)
		'''
		return self.patient_set.count() > 1

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
		('DOG', 'Dog'),
		('CAT', 'Cat'),
		('BIRD', 'Bird'),
		('REPTILE', 'Reptile'),
		('RABBIT', 'Rabbit'),
		('FISH', 'Fish'),
		('UNKOWN', 'unkown'),
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
		ordering = ["pet_name"]

class Appointment(models.Model):
	#The Appointment table, with AppointmentID as primary key
	#The paitent is a foreign key, as there can only be one paitent pr. appointment
	"""
	TODO: Create class docstring
	"""
	appointmentID = models.BigAutoField(primary_key=True)
	patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

class Breed(models.Model):
	animal = models.CharField(max_length=50, choices=Patient.Animal_Type_Choices, default='Unknown')
	breed = models.CharField(max_length=200, default='Unknown')
