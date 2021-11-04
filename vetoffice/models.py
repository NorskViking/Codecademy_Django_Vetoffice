from django.db import models
#TODO: Create Docstring comments for classes and functions
from patient.models import Patient
from employee.models import Employee

class Appointment(models.Model):
	#The Appointment table, with AppointmentID as primary key
	#The paitent is a foreign key, as there can only be one paitent pr. appointment
	"""
	TODO: Create class docstring
	"""
	appointmentID = models.BigAutoField(primary_key=True)
	patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
	employeeID = models.ForeignKey(Employee, on_delete=models.CASCADE)
