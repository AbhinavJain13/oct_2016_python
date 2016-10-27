from __future__ import unicode_literals

from django.db import models

class Users(models.Model):
    name = models.TextField()
    email = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    # def __str__(self):
	# 	return self.name()

class Friendships(models.Model):
    user = models.ForeignKey('Users',related_name='usersfriend')
    friend = models.ForeignKey('Users', related_name='friendsfriend')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
