__author__ = 'tdgunes'

from django.db import models
from . import Examination


class Surgery(models.Model):
    # MASI - MAndatory Surgery Information
    examination = models.ForeignKey(Examination)
    title = models.CharField(max_length=200, null=False, blank=False)
    date = models.DateField(null=False, blank=False)


    # OSI - Optional Surgery Information
    notes = models.TextField(max_length=1000, null=True, blank=True)
    duration = models.CharField(max_length=40, null=True, blank=True)
    complications = models.CharField(max_length=200, null=True, blank=True)
    equipments = models.CharField(max_length=200, null=True, blank=True)

    def __unicode__(self):
        return "{0}".format(self.title)
