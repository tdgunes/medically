__author__ = 'tdgunes'

from django.db import models
from .examination import Examination


class Followup(models.Model):
    # MASI - MAndatory Surgery Information
    examination = models.ForeignKey(Examination)
    date = models.DateField(null=False, blank=False)


    # OSI - Optional Surgery Information
    information = models.TextField(max_length=1000, null=True, blank=True)
    appointment_date = models.DateField(null=True, blank=True)

    def __unicode__(self):
        return self.full_name