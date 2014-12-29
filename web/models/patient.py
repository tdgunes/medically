__author__ = 'tdgunes'


from django.db import models

class Patient(models.Model):
    GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'))

    # MAPI - MAndatory Patient Information
    full_name = models.CharField('Name & Surname', max_length=50, null=False, blank=False)
    city = models.CharField(max_length=40, null=False, blank=False)
    date_of_birth = models.DateField('Date Born', null=False, blank=False)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=False, blank=False)



    # OPI - Optional Patient Information
    email = models.EmailField(null=True, blank=True)
    town = models.CharField(max_length=40, null=True, blank=True)
    country = models.CharField(max_length=40, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(max_length=1000, null=True, blank=True)
    mobile_phone = models.CharField(max_length=20, null=True, blank=True)
    home_phone = models.CharField(max_length=20, null=True, blank=True)
    business_phone = models.CharField(max_length=20, null=True, blank=True)
    internal_business_phone = models.CharField(max_length=20, null=True, blank=True)
    social_security_number = models.CharField("Social Security Number", max_length=100, null=True, blank=True)
    photo = models.ImageField(upload_to='web/static/patient_photos/%Y/%m/%d/%h/', null=True, blank=True)

    def __unicode__(self):
        return self.full_name
