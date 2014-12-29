# -*- coding: utf-8 -*-
__author__ = 'tdgunes'

from ..models import Doctor, Patient
import datetime, random, time



NAMES = [("Hasan Huseyin Uyumaz","Ankara"),
         ("Bahadir Kirdan", "Istanbul"),
         ("Burak Atalay", "Adiyaman"),
         ("Bahadir Kandemir", "Mersin"),
         ("Yunus Yilmaz","Sivas"),
         ("Enes Senel","Istanbul"),
         ("Can Gocmen","Istanbul"),
         ("Berkay Cesur","Istanbul"),
         ("Yunus Jr Yilmaz","Istanbul"),
         ("Omer Kala","Istanbul"),
         ("Murat Kirtay","Istanbul"),
         ("Onur Baris Dev","Istanbul"),
         ("Taha Dogan Gunes","Istanbul"),
         ("Hakan Uyumaz","Istanbul"),
         ("Deniz Sokmen","Istanbul"),
         ("Omurcan Gungoren","Istanbul"),
         ("Ata Kule","Istanbul"),
         ("Ogun Yaka","Istanbul"),
         ("Sercan Sumer","Istanbul"),
         ("Eren Sezener","Istanbul"),
         ("Burak Tutanlar","Istanbul"),
         ("Ugur Ozkan","Istanbul"),
         ("Omer Aslan","Istanbul"),
         ("Vidal Hara","Istanbul"),
         ("Arman Garip","Istanbul"),
         ("Uras Isik","Istanbul"),
         ("Ali Veli","Istanbul")
         ]




def load_super_users(apps, schema_editor):
    Doctor.objects.create_superuser(full_name="Taha Dogan Gunes", email="tdgunes@gmail.com", password="123456",
                                    title="D",
                                    institution="Göztepe Medical Park")
    Doctor.objects.create_superuser(full_name="Hakan Uyumaz", email="hakanuyumaz@gmail.com", password="123456",
                                    title="A",
                                    institution="Acıbadem Universiteis")

    print("\n\nLoad Super Users:")
    for user in Doctor.objects.all():
        print(user)

    start = time.time()
    for name, city in NAMES:
        now = datetime.datetime.now() - datetime.timedelta(random.randint(10,10000))
        gender = random.choice(["M","F"])
        patient = Patient.objects.create(full_name=name, gender=gender, date_of_birth=now, city=random.choice(["Tokat",
                                                                                                               "Eskisehir",
                                                                                                               "Istanbul",
                                                                                                               "Samsun",
                                                                                                               "Ankara",
                                                                                                               "Van",
                                                                                                               "Gaziantep",
                                                                                                               "Igdir",
                                                                                                               "Mersin",
                                                                                                               "Afyon",
                                                                                                               "Izmir",
                                                                                                               "Yozgat",
                                                                                                               "Sivas",
                                                                                                               "Nigde",
                                                                                                               "Adiyaman",
                                                                                                               "Karaman",
                                                                                                               "Gumushane",
                                                                                                               "Sinop",
                                                                                                               "Giresun",
                                                                                                               "Trabzon"]))
        print "Loading: ", patient
        patient.save()
    end = time.time()


    print "Asserting insert time:", end - start
    assert end-start < 1.0

def unload_super_users(apps, schema_editor):
    Doctor.objects.all().delete()
    Patient.objects.all().delete()




