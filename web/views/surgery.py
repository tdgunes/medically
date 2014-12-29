__author__ = 'huyumaz'

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from ..forms import SurgeryForm
from ..models import Patient, Examination, Surgery


def get_name(user):
    return user.full_name


def new_surgery_view(request, patient_id, examination_id):
    if not request.user.is_authenticated():
        return redirect("homepage")
    else:
        full_name = get_name(request.user)
        patient = get_object_or_404(Patient, pk=patient_id)
        examination = get_object_or_404(Examination, pk=examination_id)
        if request.method == "POST":
            form = SurgeryForm(request.POST)
            if form.errors or not patient:
                print form.errors
                return render(request, 'surgery.html',
                              {"errors": form.errors, "user": request.user,
                               "full_name": request.user.full_name, "patient": patient, "examination": examination})
            surgery = form.save(commit=False)
            surgery.examination = examination
            surgery.save()
            return redirect("examination", patient_id=patient_id, examination_id=examination_id)
        else:
            return render(request, 'surgery.html',
                      {"user": request.user, "full_name": full_name, "patient": patient, "examination": examination})


def surgery_view(request, patient_id, examination_id, surgery_id):
    if not request.user.is_authenticated():
        return redirect("homepage")
    else:
        patient = get_object_or_404(Patient, pk=patient_id)
        examination = get_object_or_404(Examination, pk=examination_id)
        surgery = get_object_or_404(Surgery, pk=surgery_id)
        if request.method == "POST":
            form = SurgeryForm(request.POST, instance=surgery)

            if form.is_valid():
                form.save()
                return redirect("surgery", patient_id, examination_id, surgery_id)
            else:
                print form.errors
                return render(request, 'surgery.html',
                              {"errors": form.errors, "user": request.user,
                               "full_name": request.user.full_name, "patient": patient,
                               "examination": examination, "surgery": surgery})
        else:
            return render(request, 'surgery.html',
                          {"user": request.user, "patient": patient,
                           "full_name": request.user.full_name,
                           "examination": examination, "surgery": surgery})
