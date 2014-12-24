__author__ = 'tdgunes'

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout



def new_examination_view(request, patient_id):
    if not request.user.is_authenticated():
        return redirect("homepage")
    else:
        p = get_object_or_404(Patient, pk=patient_id)
        return render(request, 'examination.html',
                      {"user": request.user, "full_name": get_name(request.user), "patient": p, "examination": True})

