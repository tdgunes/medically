# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

import django.utils.timezone
from . import load_super_users, unload_super_users


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('email', models.EmailField(unique=True, max_length=255, verbose_name=b'email address')),
                ('full_name', models.CharField(max_length=50, verbose_name=b'Name & Surname')),
                ('title', models.CharField(max_length=50, verbose_name=b'Title', choices=[(b'D', b'Dr.'), (b'P', b'Prof. Dr.'), (b'A', b'Asst. Prof.'), (b'C', b'Assoc. Prof')])),
                ('institution', models.CharField(max_length=50, verbose_name=b'Institution')),
                ('activation_key', models.CharField(max_length=40, blank=True)),
                ('activation_expire_date', models.DateTimeField()),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Examination',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'blank', max_length=100, verbose_name=b'Title')),
                ('date', models.DateField(verbose_name=b'Examination Date')),
                ('information', models.CharField(max_length=1000, null=True, verbose_name=b'Examination Information', blank=True)),
                ('diagnosis', models.CharField(max_length=1000, null=True, verbose_name=b'Diagnosis', blank=True)),
                ('offered_treatment', models.CharField(max_length=20, null=True, verbose_name=b'Offered Treatment', blank=True)),
                ('surgery_type', models.CharField(max_length=20, null=True, verbose_name=b'Surgery Type', blank=True)),
                ('surgery_date', models.DateField(null=True, verbose_name=b'Surgery Date', blank=True)),
                ('surgery_prep', models.CharField(max_length=1000, null=True, verbose_name=b'Surgery Preparation', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('full_name', models.CharField(max_length=50, verbose_name=b'Name & Surname')),
                ('city', models.CharField(max_length=40)),
                ('date_of_birth', models.DateField(verbose_name=b'Date Born')),
                ('gender', models.CharField(max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('email', models.EmailField(max_length=75, null=True, blank=True)),
                ('town', models.CharField(max_length=40, null=True, blank=True)),
                ('country', models.CharField(max_length=40, null=True, blank=True)),
                ('address', models.CharField(max_length=200, null=True, blank=True)),
                ('description', models.TextField(max_length=1000, null=True, blank=True)),
                ('mobile_phone', models.CharField(max_length=20, null=True, blank=True)),
                ('home_phone', models.CharField(max_length=20, null=True, blank=True)),
                ('business_phone', models.CharField(max_length=20, null=True, blank=True)),
                ('internal_business_phone', models.CharField(max_length=20, null=True, blank=True)),
                ('social_security_number', models.CharField(max_length=100, null=True, verbose_name=b'Social Security Number', blank=True)),
                ('photo', models.ImageField(null=True, upload_to=b'web/static/patient_photos/%Y/%m/%d/%h/', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='examination',
            name='patient',
            field=models.ForeignKey(to='web.Patient'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='doctor',
            name='examinations',
            field=models.ManyToManyField(to='web.Examination'),
            preserve_default=True,
        ),
        migrations.RunPython(load_super_users, reverse_code=unload_super_users),
    ]
