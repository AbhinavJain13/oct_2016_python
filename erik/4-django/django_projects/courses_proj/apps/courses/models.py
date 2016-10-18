from __future__ import unicode_literals
# import request
import re

from django.db import models

# MODELS ----------------------------------

class CustomManager(models.Manager):
    print('*'*20)
    print('CUSTOM MANAGER CALLED')
    print('*'*20)
    def validate_textarea(self,txt):
        pass

    def validate(self,email):
        print('*'*20)
        print('VALIDATE EMAIL CALLED')
        print('*'*20)
        # re.match(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', email):
        if re.match(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', email):
            print('*'*20)
            print('EMAIL MATCH!!')
            print('*'*20)
            return(True)
        else:
            print('*'*20)
            print('EMAIL FAIL!!')
            print('*'*20)
            return(False)

    def login(self,email):
        # add to db
        u = User.objects.create(email=email)

        return(u)

    def logout(self):
        del request.session['logged_in']
        return(True)

class User(models.Model):
    email = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    objects = CustomManager()

class Course(models.Model):
    name = models.TextField(default=None)
    user = models.ForeignKey(User, default=None)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class Description(models.Model):
    description = models.TextField()
    user = models.ForeignKey(User,default=None)
    course = models.OneToOneField(
        Course,
        on_delete=models.CASCADE,
        primary_key=True,
        default=None,
        related_name='description'
    )
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User,default=None)
    course =  models.ForeignKey(Course,default=None)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
