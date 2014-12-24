from django.contrib import admin

# Register your models here.

from django.contrib import admin

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


admin.site.register(Patient, PatientAdmin)
admin.site.register(Examination, ExaminationAdmin)
admin.site.register(Doctor)