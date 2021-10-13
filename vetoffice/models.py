from django.db import models

# Create your models here.
class Owner(models.Model):
	#The Owner table, with OwnerID as primary key
	#Owner can own several pets
	ownerID = models.CharField(max_length=30, primary_key=True)
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	phone = models.CharField(max_length=30)
	pass

class Patient(models.Model):
	#The Patient table, with patientID as primary key
	#Owner is foreign key, as the paitent can only have one owner
	patientID = models.CharField(max_length=30, primary_key=True)
	pet_name = models.CharField(max_length=200)
	owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
	animalType = models.CharField(max_length=200)
	age = models.IntegerField(default=0)
	pass

class Appointment(models.Model):
	#The Appointment table, with AppointmentID as primary key
	#The paitent is a foreign key, as there can only be one paitent pr. appointment
	appointmentID = models.CharField(max_length=30, primary_key=True)
	patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
	pass