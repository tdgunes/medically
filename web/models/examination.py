__author__ = 'tdgunes'


from django.db import models
from . import Patient

class Examination(models.Model):

    patient = models.ForeignKey(Patient)
    title = models.CharField("Title", max_length=100, null=False, default="blank")
    date = models.DateField("Examination Date", null=False)
    information = models.CharField("Examination Information", max_length=1000, null=True, blank=True)
    diagnosis = models.CharField("Diagnosis", max_length=1000, null=True, blank=True)
    offered_treatment = models.CharField("Offered Treatment", max_length=20, null=True, blank=True)
    surgery_type = models.CharField("Surgery Type", max_length=20, null=True, blank=True)
    surgery_date = models.DateField("Surgery Date", null=True, blank=True)
    surgery_prep = models.CharField("Surgery Preparation", max_length=1000, null=True, blank=True)


    def __unicode__(self):
        return self.patient.name_surname