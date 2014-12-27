# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('web', '0002_auto_20141227_1731'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='examination',
            name='observation',
        ),
        migrations.RemoveField(
            model_name='examination',
            name='planned_surgery_date',
        ),
        migrations.AddField(
            model_name='examination',
            name='diagnosis',
            field=models.CharField(max_length=1000, null=True, verbose_name=b'Diagnosis'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='examination',
            name='surgery_date',
            field=models.DateField(null=True, verbose_name=b'Surgery Date'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='examination',
            name='surgery_prep',
            field=models.CharField(max_length=1000, null=True, verbose_name=b'Surgery Preparation'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='examination',
            name='title',
            field=models.CharField(default=b'blank', max_length=20, verbose_name=b'Title'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='examination',
            name='information',
            field=models.CharField(max_length=1000, null=True, verbose_name=b'Examination Information'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='examination',
            name='offered_treatment',
            field=models.CharField(max_length=20, null=True, verbose_name=b'Offered Treatment'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='examination',
            name='surgery_type',
            field=models.CharField(max_length=20, null=True, verbose_name=b'Surgery Type'),
            preserve_default=True,
        ),
    ]
