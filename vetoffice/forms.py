from django.forms import ModelForm
from django import forms
from django.forms.widgets import SelectDateWidget, TimeInput

from vetoffice.models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('patient', 'day', 'time', 'information')
        widgets = {
            'day': SelectDateWidget(),
            #'time': forms.TimeInput(attrs={'type': 'time'}),
        }
