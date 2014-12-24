__author__ = 'tdgunes'

import hashlib
import random
import hashlib
import datetime
import uuid

def generate_token_with_email(email):
    random_string = str(random.random()).encode('utf8')
    salt = hashlib.sha1(random_string).hexdigest()[:5]
    salted = (salt + email).encode('utf8')
    activation_key = hashlib.sha1(salted).hexdigest()
    return activation_key