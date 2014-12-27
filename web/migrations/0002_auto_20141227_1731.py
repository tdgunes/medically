# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='born_date',
            new_name='date_of_birth',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='name_surname',
            new_name='full_name',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='picture',
        ),
        migrations.AddField(
            model_name='patient',
            name='photo',
            field=models.ImageField(null=True, upload_to=b'patient_photos/', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='patient',
            name='address',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='business_phone',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='country',
            field=models.CharField(max_length=40, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='description',
            field=models.TextField(max_length=1000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='email',
            field=models.EmailField(max_length=75, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='home_phone',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='internal_business_phone',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='mobile_phone',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='social_security_number',
            field=models.CharField(max_length=100, null=True, verbose_name=b'Social Security Number', blank=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='town',
            field=models.CharField(max_length=40, null=True, blank=True),
        ),
    ]
