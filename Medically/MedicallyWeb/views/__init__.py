__author__ = 'tdgunes'

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout

from .doctor import profile_view, registration_view, login_main_page, logout_view
from .patient import new_patient_view, patient_view
from .examination import new_examination_view



def homepage(request):
    if request.method == "POST":
        if not request.user.is_authenticated():
            email = request.POST.get('username', None)
            password = request.POST.get('password', None)

            print email, password

            if email and password:
                user = authenticate(email=email, password=password)
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
                return render(request, 'index.html', {"error": True, "error_message": "Missing credentials, try again!"})
        else:
            return login_main_page(request, request.user)
    else:
        if request.user.is_authenticated():
            return login_main_page(request, request.user)
        else:
            return render(request, 'index.html', {"error": False, "error_message": ""})