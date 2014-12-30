__author__ = 'huyumaz'

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from ..forms import FollowupForm
from ..models import Patient, Examination, Followup


def get_name(user):
    return user.full_name


def new_followup_view(request, patient_id, examination_id):
    if not request.user.is_authenticated():
        return redirect("homepage")
    else:
        full_name = get_name(request.user)
        patient = get_object_or_404(Patient, pk=patient_id)
        examination = get_object_or_404(Examination, pk=examination_id)
        if request.method == "POST":
            form = FollowupForm(request.POST)
            if form.errors or not patient or not examination:
                print form.errors
                return render(request, 'examination.html',
                              {"errors": form.errors, "user": request.user,
                               "full_name": full_name, "patient": patient, "examination": examination})
            followup = form.save(commit=False)
            followup.examination = examination
            followup.save()
            return redirect("examination", patient_id=patient_id, examination_id=examination_id)
        else:
            return render(request, 'followup.html',
                          {"user": request.user, "full_name": full_name, "patient": patient,
                           "examination": examination})


def followup_view(request, patient_id, examination_id, followup_id):
    if not request.user.is_authenticated():
        return redirect("homepage")
    else:
        patient = get_object_or_404(Patient, pk=patient_id)
        examination = get_object_or_404(Examination, pk=examination_id)
        followup = get_object_or_404(Followup, pk=followup_id)
        if request.method == "POST":
            form = FollowupForm(request.POST, instance=Followup)

            if form.is_valid():
                form.save()
                return redirect("followup", patient_id, examination_id, followup_id)
            else:
                print form.errors
                return render(request, 'followup.html',
                              {"errors": form.errors, "user": request.user,
                               "full_name": request.user.full_name, "patient": patient,
                               "examination": examination, "followup": followup})
        else:
            return render(request, 'followup.html',
                          {"user": request.user, "patient": patient,
                           "full_name": request.user.full_name,
                           "examination": examination, "followup": followup})
