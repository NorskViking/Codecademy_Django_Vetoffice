from django.test import TestCase

from owner.models import Owner
from patient.models import Animal, Breed, Patient
# Create your tests here.

class OwnerModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Owner.objects.create(first_name='TestFirstName', last_name='TestLastName', phone='TestPhone')

        dog = Animal.objects.create(animal_type='Dog')
        breed = Breed.objects.create(animal=dog, breed='Yorkshire')
        patient1 = Patient.objects.create(pet_name="TestPet1", animal=dog, breed=breed, age=2, owner=Owner.objects.get(id=1))
        patient2 = Patient.objects.create(pet_name="TestPet2", animal=dog, breed=breed, age=2, owner=Owner.objects.get(id=1))


    def test_first_name_label(self):
        owner = Owner.objects.get(id=1)
        field_label = owner._meta.get_field('first_name').verbose_name
        self.assertEqual(field_label, 'first name')

    def test_first_name_max_length(self):
        owner = Owner.objects.get(id=1)
        max_length = owner._meta.get_field('first_name').max_length
        self.assertEqual(max_length, 100)

    def test_last_name_label(self):
        owner = Owner.objects.get(id=1)
        field_label = owner._meta.get_field('last_name').verbose_name
        self.assertEqual(field_label, 'last name')

    def test_last_name_max_length(self):
        owner = Owner.objects.get(id=1)
        max_length = owner._meta.get_field('last_name').max_length
        self.assertEqual(max_length, 100)

    def test_object_name_is_last_name_comma_first_name(self):
        owner = Owner.objects.get(id=1)
        expected_object_name = f'{owner.last_name}, {owner.first_name}'
        self.assertEqual(str(owner), expected_object_name)

    def test_object_owns_multiple_pets(self):
        owner = Owner.objects.get(id=1)
        self.assertTrue(owner.has_multiple_pets())
