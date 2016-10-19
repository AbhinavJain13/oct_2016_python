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
            print('USER INFO VALIDATED! CREATING USER...')
            new_user = User.objects.create(first_name=params['first_name'],last_name=params['last_name'],email=params['email'],password=validations.gen_password(params['pw1']))
            print('NEW USER:',new_user)
            return {'result': True,'user':new_user}

    def login(self,email,password):
        # validate
        if validations.validate_email(email):
            # process
            errors = {}
            # find returns a list, can be empty
            # TODO : RETURNS ERROR, SAME THING WITH THE USER MODEL
            u = User.objects.filter(email=email)
            print('User to attempt login: ',u[0])
            print('password: ',u[0].password)
            if u[0]:
                # compare hashed pw entered against hashed pw stored
                if bcrypt.hashpw(password,bcrypt.gensalt()) == u[0].password:
                    return {'self': u[0]}
                else:
                    return False
            else:
                return False
                #return {'errors':'Not found!'}
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
