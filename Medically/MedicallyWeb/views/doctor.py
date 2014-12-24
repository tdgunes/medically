__author__ = 'tdgunes'

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout


from ..models import Patient



def profile_view(request):
    if not request.user.is_authenticated():
        return redirect("homepage")
    else:
        name = request.POST.get('name', None)
        username = request.POST.get('username', None)
        email = request.POST.get('email', None)
        full_name = get_name(request.user)

        if name and username and email:
            print name, username, email
            user_from_db = User.objects.get(username__exact=request.user.username)
            user_from_db.username = username
            user_from_db.email = email
            user_from_db.first_name = name
            user_from_db.save()

        return render(request, 'profile.html', {"full_name": user.full_name})


def login_main_page(request, user):
    patients = Patient.objects.all()
    return render(request, 'patients.html', {"full_name": user.full_name, "patients": patients, "examination": False})


def logout_view(request):
    logout(request)
    return redirect("homepage")


def registration_view(request):
    if request.user.is_authenticated():
        return redirect("homepage")
    else:
        return render(request, 'register.html')