__author__ = 'tdgunes'

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.forms import ModelForm
from ..models import Patient
from ..forms import PatientForm

def get_name(user):
    return user.full_name

def new_patient_view(request):
    if not request.user.is_authenticated():
        return redirect("homepage")
    else:
        full_name = get_name(request.user)
        if request.method == "POST":
            print request.POST
            form = PatientForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("homepage")


            return render(request, 'patient.html',
                      {"user": request.user, "full_name": get_name(request.user),"errors":form.errors})
        else:

            return render(request, 'patient.html',
                      {"user": request.user, "full_name": get_name(request.user)})


def patient_view(request, patient_id):
    if not request.user.is_authenticated():
        return redirect("homepage")
    else:
        p = get_object_or_404(Patient, pk=patient_id)

        if request.method == "POST":
            form = PatientForm(request.POST, instance=p)
            if form.is_valid():
                form.save()

                return redirect("patient", patient_id)
            else:
                return render(request, 'patient.html',
                      {"user": request.user, "full_name": get_name(request.user), "patient": p, "examination": True,
                       "examinations": p.examination_set.all(),"errors":form.errors})

        return render(request, 'patient.html',
                      {"user": request.user, "full_name": get_name(request.user), "patient": p, "examination": True,
                       "examinations": p.examination_set.all()})

