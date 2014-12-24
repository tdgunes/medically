from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.forms import ModelForm
from MedicallyWeb.models import Patient
from django.contrib.auth.models import User


# Create your views here.

def get_name(user):
    full_name = user.first_name
    if full_name.strip() == "":
        full_name = user.username
    return full_name


def new_patient_view(request):
    if not request.user.is_authenticated():
        return redirect("homepage")
    else:
        full_name = get_name(request.user)
        return render(request, 'patient.html',
                      {"user": request.user, "full_name": get_name(request.user)})

class PatientForm(ModelForm):
    class Meta:
        model = Patient
        localized_fields = ('born_date',)

def patient_view(request, patient_id):
    if not request.user.is_authenticated():
        return redirect("homepage")
    else:
        p = get_object_or_404(Patient, pk=patient_id)
        if request.method == "POST":
            print p

            form = PatientForm(request.POST, instance=p)

            if form.is_valid():
                form.save()
                print "ss"
                return redirect("patient_view", patient_id)
            else:
                return render(request, 'patient.html',
                      {"user": request.user, "full_name": get_name(request.user), "patient": p, "examination": True,
                       "examinations": p.examination_set.all(),"errors":form.errors})

        return render(request, 'patient.html',
                      {"user": request.user, "full_name": get_name(request.user), "patient": p, "examination": True,
                       "examinations": p.examination_set.all()})


def homepage(request):
    if not request.user.is_authenticated():
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        if username and password:
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    # Redirect to a success page
                    return redirect("homepage")
                else:
                    # Return a 'disabled account' error message
                    return render(request, 'index.html',
                                  {"error": True, "error_message": "Your account is disabled!"})

            else:
                # Return an 'invalid login' error message.
                return render(request, 'index.html',
                              {"error": True, "error_message": "Wrong credentials, try again!"})
        else:
            return render(request, 'index.html', {"error": False, "error_message": ""})
    else:
        return login_main_page(request, request.user)

def login_main_page(request, user):
    full_name = get_name(user)
    patients = Patient.objects.all()
    return render(request, 'patients.html',
                  {"full_name": full_name, "patients": patients, "examination": False})

def logout_view(request):
    logout(request)
    return redirect("homepage")


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
            full_name = name

        return render(request, 'profile.html', {"full_name": full_name})

def new_examination_view(request, patient_id):
    if not request.user.is_authenticated():
        return redirect("homepage")
    else:
        p = get_object_or_404(Patient, pk=patient_id)
        return render(request, 'examination.html',
                      {"user": request.user, "full_name": get_name(request.user), "patient": p, "examination": True})