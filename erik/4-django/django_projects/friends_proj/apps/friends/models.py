from __future__ import unicode_literals

from django.db import models

# MODELS -------------------------------------

class UserManager(models.Manager):

    def login(self, email, password):
        print('*'*20)
        print('LOGIN MANAGER')
        print('*'*20)
        return('this is what im talking about brick')

    def register(self, **kwargs):
        print('*'*20)
        print('REGISTER MANAGER')
        print('*'*20)

        pass


class Blogs(models.Model):
    title = models.CharField(max_length=100)
    post = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class Comments(models.Model):
    comment = models.TextField()
    blog = models.ForeignKey(Blogs)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
