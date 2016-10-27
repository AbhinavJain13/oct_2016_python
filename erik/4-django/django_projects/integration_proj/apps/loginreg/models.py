from __future__ import unicode_literals
from django.db import models
# from .mgr import UserManager
import re
import bcrypt
import validations

# MODELS --------------------------------------

class UserManager(models.Manager):
    def register(self,params):
        print('REGISTRATION IN PROCESS...')
        errors = {}

        if not validations.validate_email(params.get('email')):
            errors['email'] = 'Invalid Email.'
            print('REGISTRATION ERRORS', errors)

        if not validations.validate_letters(params.get('first_name'),2):
            errors['first_name'] = 'Invalid First Name.'
            print('REGISTRATION ERRORS', errors)

        if not validations.validate_letters(params.get('last_name'),2):
            errors['last_name'] = 'Invalid Last Name.'
            print('REGISTRATION ERRORS', errors)

        if not validations.match_strings(params.get('pw1'),params.get('pw2')):
            errors['password'] = 'Passwords do not match!'
            print('REGISTRATION ERRORS', errors)

        if not validations.validate_length(params.get('pw1'),8) and not validations.validate_length(params.get('pw2'),8):
            errors['password'] = 'Passwords need to be 8 characters!'
            print('REGISTRATION ERRORS', errors)

        if errors:
            print('-> FAILED REGISTRATION <-', errors)
            result = {'result': False, 'errors': errors}
            return {'result': False, 'errors': errors}

        else:
            print('USER INFO VALIDATED! CREATING USER...',params['pw1'])
            new_user = User.objects.create(first_name=params['first_name'],last_name=params['last_name'],email=params['email'],password=validations.gen_password(params['pw1']))
            print('NEW USER:',new_user)
            return {'result': True,'user':new_user}

    def login(self,email,password):
        if validations.validate_email(email):
            # process
            errors = {}
            # .filter() returns a dict, can be empty
            # .get() will return an object, errors on not found. so...
            try:
                u = User.objects.get(email=email)
                print('USER FOUND, CHECKING PASSWORD... ',u)

                if bcrypt.hashpw(password.encode(),u.password) == u.password:
                    return {'self': u}
                else:
                    print('INVALID PASSWORD')
                    return {'errors':'Password incorrect!'}
            except:
                print('INVALID EMAIL')
                return {'errors':'Email not found!'}
        else:
            return False

class User(models.Model):
    first_name = models.TextField(max_length=200)
    last_name = models.TextField(max_length=200)
    email = models.TextField(max_length=200)
    password = models.TextField(max_length=300,default='password error')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    objects = UserManager()
