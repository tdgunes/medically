__author__ = 'tdgunes'


from django.db import models
from . import Patient

class Examination(models.Model):

    patient = models.ForeignKey(Patient)
    title = models.CharField("Title", max_length=20, null=False)
    date = models.DateField("Examination Date", null=False)
    information = models.CharField("Examination Information", max_length=1000)
    diagnosis = models.CharField("Diagnosis", max_length=1000)
    offered_treatment = models.CharField("Offered Treatment", max_length=20)
    surgery_type = models.CharField("Surgery Type", max_length=20, null=True)
    surgery_date = models.DateField("Surgery Date", null=True)
    surgery_prep = models.CharField("Surgery Preparation", max_length=1000)


    def __unicode__(self):
        return self.patient.name_surname