from django.forms import ModelForm, TextInput

from owner.models import Owner

class OwnerForm(ModelForm):
    class Meta:
        model = Owner
        fields = ['first_name', 'last_name', 'phone']
        labels = {
            'first_name' : 'First name:',
            'last_name' : 'Family name:',
            'phone' : 'Phone'
        }
