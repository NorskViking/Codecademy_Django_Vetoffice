from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus

from owner.forms import OwnerForm
from owner.models import Owner
# Create your tests here.
class TestOwnerForm(TestCase):

    def test_owner_form(self):
        #form = OwnerForm()
        data = {
            'first_name': 'TestFirstName',
            'last_name': 'TestLastName',
            'phone': '00000000',
        }
        response = self.client.get(reverse('owner:ownercreate'))
        self.assertTemplateUsed(response, 'owner_create_form.html')
        self.assertContains(response, 'first_name')
        self.assertContains(response, 'last_name')
        self.assertContains(response, 'phone')
        response = self.client.post(reverse('owner:ownercreate'), data=data)
        self.assertEqual(Owner.objects.count(), 1)
        self.assertRedirects(response, reverse('owner:ownerlist'))


    def test_first_name_is_lowercase(self):
        response = self.client.post('register', data={'first_name': 'testlowerfirstcasename', 'last_name': 'testlowercaselastname', 'phone':'45631661'})
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, 'Should start with uppercase letter', html=True)
