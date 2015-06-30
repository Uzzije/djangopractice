
import re
from first_blog import models

NAME_VALID = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")

def sign_up_entry_validation(user_name, password, verify_password, email):
    user_name_valid = sign_up_check_valid_name(user_name)
    email_valid = check_valid_email(email)
    passwords_valid = sign_up_password_valid(password, verify_password)
    if user_name_valid == "" and passwords_valid == "" and email_valid == "":
        return True
    else:
        return False


def sign_up_password_valid(first_password, verifying_password):
    if first_password == verifying_password and NAME_VALID.match(first_password) is not None:
        return ""
    else:
        return "Password does not match or does not meet the text criteria!"


def deos_name_exist(name):
    try:
        user = models.Author.objects.get(user_name=name)
    except models.Author.DoesNotExist:
        user = None
    return user

def sign_up_check_valid_name(name):
    name_valid = NAME_VALID
    if name_valid.match(name) is None or deos_name_exist(name) is not None:
        return "Invalid Input!"
    else:
        return ""

def check_valid_email(email):
    email_valid = re.compile("[^@]+@[^@]+\.[^@]+$")
    if email == '':
        return ''
    else:
        if email_valid.match(email):
            return ''
        else:
            return "Invalid Email"


def log_in_check_valid_entry(name, password):
    user = deos_name_exist(name)
    if user:
        if user.password == password:
            return True
        else:
            return False
    return False





