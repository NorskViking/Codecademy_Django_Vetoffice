from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus

from employee.forms import EmployeeForm
from employee.models import Employee
# Create your tests here.
class TestEmployeeForm(TestCase):

    def test_employee_form(self):

        data = {
            'title': 'Dr.',
            'first_name': 'TestFirstName',
            'last_name': 'TestLastName',
            'phone': '00000000',
            'email': 'TestLastName@vetoffice.com',
        }
        response = self.client.get(reverse('employee:employeecreate'))
        self.assertTemplateUsed(response, 'employee_create_form.html')
        self.assertContains(response, 'title')
        self.assertContains(response, 'first_name')
        self.assertContains(response, 'last_name')
        self.assertContains(response, 'phone')
        self.assertContains(response, 'email')
        response = self.client.post(reverse('employee:employeecreate'), data=data)
        self.assertEqual(Employee.objects.count(), 1)
        self.assertRedirects(response, reverse('employee:employeelist'))


    def test_first_name_is_lowercase(self):
        response = self.client.post('register', data={'first_name': 'testlowerfirstcasename', 'last_name': 'testlowercaselastname', 'phone':'45631661'})
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, 'Should start with uppercase letter', html=True)
