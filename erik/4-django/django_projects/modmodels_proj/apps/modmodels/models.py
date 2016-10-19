from __future__ import unicode_literals

from django.db import models

# Models ---------------------------------------

class Users(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30,default='erik@erik.com', editable=False)
    password = models.CharField(max_length=30, default='0000000', editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
class Msgs(models.Model):
    user_id = models.ForeignKey(Users)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
class Comments(models.Model):
    user_id = models.ForeignKey(Users)
    message_id = models.ForeignKey(Msgs)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
