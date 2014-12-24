__author__ = 'tdgunes'

from django.forms import ModelForm


class PatientForm(ModelForm):
    class Meta:
        model = Patient
        localized_fields = ('born_date',)