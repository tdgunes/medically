__author__ = 'tdgunes'


from django.db import models
from . import Patient

class Examination(models.Model):
    TREATMENT_OFFERS = (('Surgery', 'Surgery'), ('Conservative', 'Conservative'))

    patient = models.ForeignKey(Patient)
    date = models.DateField("Examination Date")
    information = models.TextField("Examination Information", max_length=1000)
    observation = models.TextField("Observation", max_length=1000)
    offered_treatment = models.CharField("Offered Treatment", max_length=20, choices=TREATMENT_OFFERS)

    surgery_type = models.CharField("Offered Treatment", max_length=20, null=True)
    planned_surgery_date = models.DateField(null=True)

    def __unicode__(self):
        return self.patient.name_surname