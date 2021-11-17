from django.db import models

# Create your models here.
class Owner(models.Model):
	#The Owner table, with OwnerID as primary key
	#Owner can own several pets
	"""Create the Owner SQLite Table.

	Primary Key: OwnerID, used as Foreign Key for paitient

	Fields: first_name(String), last_name(string), phone(Integer)

	__str__ for easy coupling first and last name of owner.

	Function: has_multiple_pets
				reurns boolean True if owner have several pets registered with the Vet Office.
	"""
	#id = models.BigAutoField(primary_key=True)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	phone = models.IntegerField()
	def __str__(self):
		#Returns the first and last name of owner with whitespace between
		return '%s, %s' % (self.last_name, self.first_name)

	def has_multiple_pets(self):
		'''Do Owner have multiple pets.

		Checks if a owner have multiple pets registered at the vet Vetoffice
		and returns a boolean.

		parameters: self

		returns: boolean (True if owned pets are greater then 1)
		'''
		return self.patient_set.count() > 1
