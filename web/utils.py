__author__ = 'tdgunes'

import hashlib
import random
import hashlib
import datetime
import uuid


from django.http import HttpResponseRedirect
from django.core.mail import EmailMessage





def generate_token_with_email(email):
    random_string = str(random.random()).encode('utf8')
    salt = hashlib.sha1(random_string).hexdigest()[:5]
    salted = (salt + email).encode('utf8')
    activation_key = hashlib.sha1(salted).hexdigest()
    return activation_key

def custom_redirect(url_name, *args, **kwargs):
    # http://stackoverflow.com/questions/3765887/add-request-get-variable-using-django-shortcuts-redirect
    from django.core.urlresolvers import reverse
    import urllib
    url = reverse(url_name, args = args)
    params = urllib.urlencode(kwargs)
    return HttpResponseRedirect(url + "?%s" % params)


def send_activation_mail(doctor):
    subject = "Activate your Medically Account - Medically"
    body = """Hello {0} {1},

Thank you for signing up for Medically.

To finish your signing up process,

Please click the link below to activate your account:

http://127.0.0.1:8000/activate/{2}/

Best Regards,
Medically Team
            """.format(doctor.get_title(), doctor.full_name, doctor.activation_key)

    mail = EmailMessage(subject, body, "Medically <info@luckyfriday.org>", to=[doctor.email])
    mail.send(fail_silently=False)


def send_activation_successful_mail(doctor):
    subject = "Your Medically Account is Now Active! - Medically"
    body = """Hello {0} {1},

Thank you for signing up for Medically.

You have now successfully activated your account.

Best Regards,
Medically Team
        """.format(doctor.get_title(), doctor.full_name)

    mail = EmailMessage(subject, body, "Medically <info@luckyfriday.org>", to=[doctor.email])
    mail.send(fail_silently=False)