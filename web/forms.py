__author__ = 'tdgunes'

from django import forms
from django.forms import ModelForm
from .models import Doctor, Patient, Examination, Surgery
from .utils import generate_token_with_email
import pytz
import datetime


class DoctorCreationForm(forms.ModelForm):
    password = forms.CharField(label='Password')

    class Meta:
        model = Doctor
        fields = ('email', 'password', 'full_name', 'institution',)


    def save(self, commit=True):
        doctor = super(DoctorCreationForm, self).save(commit=False)

        doctor.set_password(self.cleaned_data["password"])
        doctor.activation_key = generate_token_with_email(self.cleaned_data["email"])
        doctor.activation_expire_date = datetime.datetime.now(pytz.utc) + datetime.timedelta(2)
        if commit:
            doctor.save()
        return doctor


class DoctorUpdateForm(forms.ModelForm):
    class Meta:
        model = Doctor
        exclude = ('password',)
        fields = ('email', 'full_name', 'institution',)


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        localized_fields = ('date_of_birth',)


class ExaminationForm(forms.ModelForm):
    class Meta:
        exclude = {'patient'}
        model = Examination


class SurgeryForm(forms.ModelForm):
    class Meta:
        model = Surgery
        exclude = {'examination'}
