__author__ = 'tdgunes'

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from ..models import Patient, Examination
from ..forms import ExaminationForm



def new_examination_view(request, patient_id):
    if not request.user.is_authenticated():
        return redirect("homepage")
    else:
        patient = get_object_or_404(Patient, pk=patient_id)
        if request.method == "POST":
            form = ExaminationForm(request.POST)

            if form.errors or not patient:
                print form.errors
                return render(request, 'examination.html',
                              {"errors": form.errors, "user": request.user,
                               "full_name": request.user.full_name, "patient": patient})

            examination = form.save()
            examination.patient = patient
            examination.save()
            return redirect("patient_view", patient_id)
        else:
            return render(request, 'examination.html',
                          {"user": request.user, "full_name": request.user.full_name, "patient": patient})

