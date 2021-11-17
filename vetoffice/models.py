from django.db import models
from django.contrib.auth.models import User
#TODO: Create Docstring comments for classes and functions
from patient.models import Patient
from employee.models import Employee

class Appointment(models.Model):
	#The Appointment table, with AppointmentID as primary key
	#The paitent is a foreign key, as there can only be one paitent pr. appointment
	"""
	TODO: Create class docstring
	"""
	patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
	#employeeID = models.ForeignKey(Employee, on_delete=models.CASCADE)
	day = models.DateField(auto_now=False, auto_now_add=False)
	time = models.TimeField(auto_now=False, auto_now_add=False)
	employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
	user = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)
	information = models.CharField(max_length=2000, default='')

	def __str__(self):
		return self.patient.__str__() + "\t" + str(self.day.day) + " " + str(self.day.month) + " " + str(self.day.year) + " " + str(self.time.hour) + " " + str(self.time.min)
