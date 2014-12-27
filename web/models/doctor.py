__author__ = 'tdgunes'

import datetime

from django.db import models

from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
import pytz

from ..utils import generate_token_with_email


class DoctorManager(BaseUserManager):
    def create_doctor(self, full_name=None, email=None, password=None, title=None, institution=None):
        if not (full_name and email and password and title and institution):
            raise ValueError('A doctor user requires full_name, email, password, title, institution')

        doctor = self.model(
            email=self.normalize_email(email),
            full_name=full_name.title(),
            title=title,
            institution=institution,
            activation_key=generate_token_with_email(self.normalize_email(email)),
            activation_expire_date=datetime.datetime.now(pytz.utc) + datetime.timedelta(2),
        )

        doctor.is_active = False
        doctor.set_password(password)
        doctor.save(using=self._db)
        return doctor

    def create_superuser(self, full_name=None, email=None, password=None, title=None, institution=None):

        doctor = self.create_doctor(
            email=self.normalize_email(email),
            password=password,
            full_name=full_name,
            title=title,
            institution=institution
        )

        doctor.is_active = True
        doctor.is_admin = True
        doctor.save(using=self._db)
        return doctor


class Doctor(AbstractBaseUser):

    TITLES = (("D", "Dr.",), ("P", "Prof. Dr."), ("A", "Asst. Prof."), ("C", "Assoc. Prof"))

    TITLES_DICT = {y:x for x,y in TITLES}
    TITLES_REVERSE_DICT = {x:y for x,y in TITLES}


    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True
    )

    full_name = models.CharField('Name & Surname', max_length=50)
    title = models.CharField('Title', max_length=50, choices=TITLES)
    institution = models.CharField('Institution', max_length=50)

    examinations = models.ManyToManyField('Examination')

    activation_key = models.CharField(max_length=40, blank=True)
    activation_expire_date = models.DateTimeField()

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name', 'title', 'institution']

    objects = DoctorManager()

    class Meta:
        pass

    def get_full_name(self):
        return self.full_name

    def get_short_name(self):
        return self.full_name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


    def get_title(self):
        return Doctor.TITLES_REVERSE_DICT[self.title]

    @property
    def is_staff(self):
        return self.is_admin

    def __unicode__(self):
        if self.is_admin:
            return "Admin: {0}".format(self.email)
        else:
            return self.email


