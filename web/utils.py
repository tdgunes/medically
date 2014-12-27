__author__ = 'tdgunes'

import hashlib
import random
import hashlib
import datetime
import uuid
from django.http import HttpResponseRedirect

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