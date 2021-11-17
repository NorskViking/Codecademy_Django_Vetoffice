from django.test import TestCase

from employee.models import Employee
from patient.models import Animal, Breed, Patient
# Create your tests here.

class EmployeeModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Employee.objects.create(first_name='TestFirstName', last_name='TestLastName', phone='TestPhone')

        dog = Animal.objects.create(animal_type='Dog')
        breed = Breed.objects.create(animal=dog, breed='Yorkshire')
        patient1 = Patient.objects.create(pet_name="TestPet1", animal=dog, breed=breed, age=2, employee=Employee.objects.get(id=1))
        patient2 = Patient.objects.create(pet_name="TestPet2", animal=dog, breed=breed, age=2, employee=Employee.objects.get(id=1))


    def test_first_name_label(self):
        employee = Employee.objects.get(id=1)
        field_label = employee._meta.get_field('first_name').verbose_name
        self.assertEqual(field_label, 'first name')

    def test_first_name_max_length(self):
        employee = Employee.objects.get(id=1)
        max_length = employee._meta.get_field('first_name').max_length
        self.assertEqual(max_length, 100)

    def test_last_name_label(self):
        employee = Employee.objects.get(id=1)
        field_label = employee._meta.get_field('last_name').verbose_name
        self.assertEqual(field_label, 'last name')

    def test_last_name_max_length(self):
        employee = Employee.objects.get(id=1)
        max_length = employee._meta.get_field('last_name').max_length
        self.assertEqual(max_length, 100)

    def test_object_name_is_title_dot_last_name(self):
        employee = Employee.objects.get(id=1)
        expected_object_name = f'{employee.title, {employee.last_name}'
        self.assertEqual(str(employee), expected_object_name)
