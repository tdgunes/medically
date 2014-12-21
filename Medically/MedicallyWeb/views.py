from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout


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
        return render(request, 'index.html', {"error": True, "error_message": "Success."})
