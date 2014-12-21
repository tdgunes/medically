from django.db import models

class Patient(models.Model):
    GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'))
    name_surname = models.CharField('Name & Surname', max_length=50, )
    born_date = models.DateField('Date Born')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    address = models.CharField(max_length=200)
    town = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    country = models.CharField(max_length=40)
    home_phone = models.CharField(max_length=20)
    business_phone = models.CharField(max_length=20)
    internal_business_phone = models.CharField(max_length=20)
    mobile_phone = models.CharField(max_length=20)
    email = models.EmailField()
    picture = models.ImageField(upload_to='patient_photos/')
    description = models.TextField(max_length=1000)
    social_security_number = models.CharField("Social Security Number", max_length=100)

    def __unicode__(self):
        return self.name_surname
