from django.test import TestCase
from django.urls import reverse

from .models import Owner, Patient, Appointment
# Create your tests here.
def create_owner(first_name, last_name, phone):
    """
    Create an Owner instance with given OwnerID, first and last name and phone
    """
    return Owner.objects.create(first_name, last_name, phone)

def create_patient(patientID, pet_name, animal_type, age, owner):
    """
    Create an Paitient instance with given patientID, pet_name, age and Owner as ForeignKey
    """
    return Patient.objects.create(patientID, pet_name, age, owner)

def create_appointment(appointmentID, patient):
    """
    Create an Appointment instance with given appointmentID and paitient as ForeignKey
    """
    return Appointment.objects.create(appointmentID, paitient)

class OwnerModelTest(TestCase):

    def test_owner_instance_was_created(self):
        # Create owner instance
        new_owner = create_owner('Hans', 'Eckman', '0101010101')

        #self.assertEqual(new_owner.ownerID, '1')
