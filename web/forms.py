__author__ = 'tdgunes'

from django import forms
from django.forms import ModelForm
from .models import Doctor, Patient
from .utils import generate_token_with_email
import pytz
import datetime

class DoctorCreationFrom(forms.ModelForm):
    password = forms.CharField(label='Password')

    class Meta:
        model = Doctor
        fields = ('email', 'password', 'full_name', 'institution',)


    def save(self, commit=True):
        doctor = super(DoctorCreationFrom, self).save(commit=False)

        doctor.set_password(self.cleaned_data["password"])
        doctor.activation_key=generate_token_with_email(self.cleaned_data["email"])
        doctor.activation_expire_date=datetime.datetime.now(pytz.utc) + datetime.timedelta(2)
        if commit:
            doctor.save()

        return doctor


class PatientForm(ModelForm):
    class Meta:
        model = Patient
        localized_fields = ('born_date',)