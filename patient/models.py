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


    class Meta:
        ordering = ['animal']

class Patient(models.Model):
    #The Patient table, with patientID as primary key
    #Owner is foreign key, as the paitent can only have one owner
    """Create the patient SQLite Table.

    Primary Key: Used as Foreign Key for Appointment

    Foreign Key: owner = Owner:ownerID

    Fields: pet_name(string), animal(ForeignKey), breed(ForeignKey)
    age(integer), owner(Foreign key, delete all on Owner removed)

    __str__ for coupling pet_name and animal_type:breed of patient.
    """
    pet_name = models.CharField(max_length=200)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    age = models.IntegerField(default=0)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)

    def __str__(self):
        #Returns pet name and animal_type
        return "%s %s" % (self.pet_name, self.animal)
    def __str__(self):
        return self.breed

    class Meta:
        ordering = ["owner"]
