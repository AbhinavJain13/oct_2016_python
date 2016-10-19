from __future__ import unicode_literals
from django.db import models
from django.core.exceptions import ObjectDoesNotExist
import re, bcrypt, string


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def login(self, request_post):
        try:
            user = self.get(email=request_post['login_email'])
            password = request_post['login_password'].encode()
            if bcrypt.hashpw(password, user.pw_hash.encode()):
                return (True, user)
        except ObjectDoesNotExist:
            pass

        return (False, ["Email/password not found."])

    def register(self, user):
        errors = []
        if len(user['first_name'])< 2:
            errors.append("First name must be at least 2 charecters.")
        if len(user['last_name']) < 2:
            errors.append("Last name must be at least 2 charecters.")
        if len(user['password']) < 8:
            errors.append("Password must be at least 8 charecters.")
        if not EMAIL_REGEX.match(user['email']):
            errors.append("Invalid email address.")
        if user['confirm_password'] != user['password']:
            errors.append("Passwords do not match.")
        if str.isalpha(user['first_name']) == False:
            errors.append("First name cannot contain a number or be blank.")
        if str.isalpha(user['last_name']) == False:
            errors.append("Last name cannot contain a number or be blank.")
        try:
            user = self.get(email=user['email'])
            errors.append("Email already in use")
        except ObjectDoesNotExist:
            pass

        if len(errors) > 0:
            return (False, errors)

        pw_hash = bcrypt.hashpw(user['password'].encode(), bcrypt.gensalt())

        returnuser = self.create(first_name=user['first_name'], last_name=user['last_name'], email=user['email'], pw_hash=pw_hash)
        print(returnuser)
        return (True, returnuser)


class User(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    pw_hash = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


    objects = UserManager()
