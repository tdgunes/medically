__author__ = 'huyumaz'

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.forms import ModelForm
from ..models import Patient, Examination


def get_name(user):
    return user.full_name


def new_surgery_view(request, patient_id, examination_id):
    if not request.user.is_authenticated():
        return redirect("homepage")
    else:
        full_name = get_name(request.user)
        patient = get_object_or_404(Patient, pk=patient_id)
        examination = get_object_or_404(Examination, pk=examination_id)
        return render(request, 'surgery.html',
                      {"user": request.user, "full_name": full_name, "patient": patient, "examination": examination})