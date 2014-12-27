__author__ = 'tdgunes'

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout

from django.utils import timezone

from ..models import Patient, Doctor
from ..forms import DoctorCreationForm
from ..utils import generate_token_with_email, custom_redirect, send_activation_mail, send_activation_successful_mail


def activation(request, activation_key):
    try:
        doctor = Doctor.objects.get(activation_key=activation_key)
    except Doctor.DoesNotExist:
        return custom_redirect("homepage", activation_key_not_found=True)

    if doctor.is_active is False:
        if doctor.activation_expire_date < timezone.now():
            doctor.activation_key = generate_token_with_mail(user.email)
            doctor.save()
            send_activation_mail(doctor)
            return custom_redirect("homepage", success_activation=True)

        doctor.is_active = True
        doctor.save()
        send_activation_successful_mail(doctor)

        return custom_redirect("homepage", success_activation=True)
    else:
        return custom_redirect("homepage", already_activated=True)


def profile_view(request):
    if not request.user.is_authenticated():
        return redirect("homepage")
    else:
        name = request.POST.get('name', None)
        username = request.POST.get('username', None)
        email = request.POST.get('email', None)
        full_name = request.user.full_name

        if name and username and email:
            # TODO: must have title, institution, password, email, full_name as in registration
            print name, username, email
            user_from_db = Doctor.objects.get(username__exact=request.user.username)
            user_from_db.username = username
            user_from_db.email = email
            user_from_db.first_name = name
            user_from_db.save()

        return render(request, 'profile.html', {"full_name": request.user.full_name})


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
        if request.method == "POST":
            form = DoctorCreationForm(request.POST)
            print form

            title = Doctor.TITLES_DICT.get(request.POST["title"], None)
            if form.errors or not title:
                print form.errors
                return render(request, 'register.html', dict(errors=form.errors))

            doctor = form.save()
            doctor.title = title
            doctor.is_active = False
            doctor.save()

            send_activation_mail(doctor)

            return custom_redirect("homepage", registration=True)
        else:
            return render(request, 'register.html')