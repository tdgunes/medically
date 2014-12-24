from django.contrib import admin
from django.contrib.auth.models import Group


from .models import Patient, Examination, Doctor


class ExaminationInline(admin.StackedInline):
    model = Examination
    extra = 0


class ExaminationAdmin(admin.ModelAdmin):

    list_display = ['patient', 'date', 'offered_treatment']
    list_filter = ['offered_treatment', 'date']


class PatientAdmin(admin.ModelAdmin):

    search_fields = ['name_surname']
    list_display = ('name_surname', 'gender', 'city')
    list_filter = ['city']
    inlines = [ExaminationInline]


class DoctorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'title','institution')
    list_filter = ['full_name', 'title','institution']

admin.site.register(Patient, PatientAdmin)
admin.site.register(Examination, ExaminationAdmin)
admin.site.register(Doctor, DoctorAdmin)

admin.site.unregister(Group)