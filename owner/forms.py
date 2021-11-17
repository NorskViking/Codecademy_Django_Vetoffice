from django.forms import ModelForm, TextInput

from owner.models import Owner

class OwnerForm(ModelForm):
    """ Owner ModelForm

    model: Owner

    fields: first_name, last_name, phone

    Functions:  clean_first_name()
                    - Cleans the data, and add errors if name does not start with uppercase or include an Integer.
                clean_last_name()
                    - Cleans the data, and add errors if name does not start with uppercase or include an Integer.
    """
    class Meta:
        model = Owner
        fields = ['first_name', 'last_name', 'phone']
        labels = {
            'first_name' : 'First name:',
            'last_name' : 'Family name:',
            'phone' : 'Phone'
        }

        def clean_first_name(self):
            first_name = self.cleaned_data['first_name']
            if not first_name:
                return first_name

            if not first_name[0].isupper():
                self.add_error('first_name', 'Should start with uppercase letter')

            if first_name.isdigit():
                self.add_error('first_name', 'Should not contain numbers')

            return first_name

        def clean_last_name(self):
            last_name = self.cleaned_data['last_name']
            if not last_name:
                return last_name

            if not last_name[0].isupper():
                self.add_error('last_name', 'Should start with uppercase letter')

            if last_name.isdigit():
                self.add_error('last_name', 'Should not contain numbers')

            return last_name
