# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MedicallyWeb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='examinations',
            field=models.ManyToManyField(to='MedicallyWeb.Examination'),
            preserve_default=True,
        ),
    ]
