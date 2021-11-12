from django.forms import ModelForm

from vetoffice.models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('patient', 'day', 'time')
