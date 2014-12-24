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
                ('date', models.DateField(verbose_name=b'Examination Date')),
                ('information', models.TextField(max_length=1000, verbose_name=b'Examination Information')),
                ('observation', models.TextField(max_length=1000, verbose_name=b'Observation')),
                ('offered_treatment', models.CharField(max_length=20, verbose_name=b'Offered Treatment', choices=[(b'Surgery', b'Surgery'), (b'Conservative', b'Conservative')])),
                ('surgery_type', models.CharField(max_length=20, null=True, verbose_name=b'Offered Treatment')),
                ('planned_surgery_date', models.DateField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_surname', models.CharField(max_length=50, verbose_name=b'Name & Surname')),
                ('born_date', models.DateField(verbose_name=b'Date Born')),
                ('gender', models.CharField(max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('address', models.CharField(max_length=200)),
                ('town', models.CharField(max_length=40)),
                ('city', models.CharField(max_length=40)),
                ('country', models.CharField(max_length=40)),
                ('home_phone', models.CharField(max_length=20)),
                ('business_phone', models.CharField(max_length=20)),
                ('internal_business_phone', models.CharField(max_length=20)),
                ('mobile_phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=75)),
                ('picture', models.ImageField(upload_to=b'patient_photos/')),
                ('description', models.TextField(max_length=1000)),
                ('social_security_number', models.CharField(max_length=100, verbose_name=b'Social Security Number')),
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
