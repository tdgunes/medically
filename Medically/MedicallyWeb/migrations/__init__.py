# -*- coding: utf-8 -*-
__author__ = 'tdgunes'

from ..models import Doctor

def load_super_users(apps, schema_editor):
    Doctor.objects.create_superuser(full_name="Taha Dogan Gunes", email="tdgunes@gmail.com", password="123456", title="Dr.",
                                    institution="Göztepe Medical Park")
    Doctor.objects.create_superuser(full_name="Hakan Uyumaz", email="hakanuyumaz@gmail.com", password="123456", title="Dr.",
                                    institution="Acıbadem Universiteis")

    print("\n\nLoad Super Users:")
    for user in Doctor.objects.all():
        print(user)


def unload_super_users(apps, schema_editor):
    Doctor.objects.all().delete()




