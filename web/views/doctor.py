__author__ = 'tdgunes'

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.core.mail import EmailMessage

from ..models import Patient, Doctor
from ..forms import DoctorCreationFrom
from ..utils import generate_token_with_email


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
            form = DoctorCreationFrom(request.POST)
            print form

            title = Doctor.TITLES_DICT.get(request.POST["title"], None)
            if form.errors or not title:
                print form.errors
                return render(request, 'register.html', dict(errors=form.errors))

            doctor = form.save()
            doctor.title = title
            doctor.save()

            subject = "Activate your Medically Account - Medically"
            body = """Hello {0} {1},

Thank you for signing up for Medically.

To finish your signing up process,

Please click the link below to activate your account:

http://127.0.0.1/activate/{2}/

Best Regards,
Medically Team
            """.format(Doctor.TITLES_REVERSE_DICT[doctor.title], doctor.full_name, doctor.activation_key)

            mail = EmailMessage(subject, body, "Medically <info@luckyfriday.org>", to=[doctor.email])
            mail.send(fail_silently=False)


            print doctor
            return redirect("homepage")
        else:
            return render(request, 'register.html')