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
	ownerID = models.CharField(max_length=30, primary_key=True)
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
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

	Fields: patientID(String), pet_name(string), animal_type(string, 2-tuple:animal type/breed),
	age(integer), owner(Foreign key, delete all on Owner removed)

	List: Animal_Type_Choices - couples itreable 2-tuples of breed connected to animal_type.

	__str__ for easy coupling pet_name and animal_type:breed of patient.
	"""
	Animal_Type_Choices = [
	#Using animal type as a group, followed with iterable 2-tuples of breed for the animal type.
		('Dog', (
				('german sheperd', 'German Sheperd'),
				('pomeranian', 'Pomeranian'),
				('labrador', 'Labrador'),
				('husky', 'Husky'),
				('bulldog', 'Bulldog'),
				('chihuahua', 'Chihuahua'),
			)
		),
		('Cat', (
				('norewgian forest cat', 'Norwegian Forest Cat'),
				('persian', 'Persian'),
				('sphynx', 'Sphynx'),
				('siamese', 'Siamese'),
				('maine coon', 'Maine Coon'),
			)
		),
		('Bird', (
				('parakeet', 'Parakeet'),
				('cockatiel', 'Cockatiel'),
				('canarie', 'Canarie'),
				('african grey', 'African Grey'),
				('amazon parrot', 'Amazon Parrot'),
			)
		),
		('Reptile', (
				('crested gecko', 'Crested Gecko'),
				('ball python', 'Ball Python'),
				('bearded dragon', 'Bearded Dragon'),
				('leopard gecko', 'Leopard Gecko'),
				('corn snake', 'Corn Snake'),
			)
		),
		('Rabbit', (
				('mini rex', 'Mini Rex'),
				('holland lop', 'Holland Lop'),
				('dutch lop', 'Dutch Lop'),
				('dwarf hotot', 'Dwarf Hotot'),
				('mini lop', 'Mini lop'),
			)
		),
		('Fish', (
				('betta', 'Betta'),
				('goldfish', 'Goldfish'),
				('angelfish', 'Angelfish'),
				('catfish', 'Catfish'),
				('guppi', 'Guppi'),
			)
		),
		('Unknown', 'unkown'),
	]
	patientID = models.CharField(max_length=30, primary_key=True)
	pet_name = models.CharField(max_length=200)
	animal_type = models.CharField(max_length=200, choices=Animal_Type_Choices, default='Unkown')
	age = models.IntegerField(default=0)
	owner = models.ForeignKey(Owner, on_delete=models.CASCADE)

	def __str__(self):
		#Returns pet name and breed
		return self.pet_name + ", " + self.animal_type

	class Meta:
		ordering = ["pet_name"]

class Appointment(models.Model):
	#The Appointment table, with AppointmentID as primary key
	#The paitent is a foreign key, as there can only be one paitent pr. appointment
	"""
	TODO: Create class docstring
	"""
	appointmentID = models.CharField(max_length=30, primary_key=True)
	patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
