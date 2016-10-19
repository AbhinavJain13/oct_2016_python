from __future__ import unicode_literals
from django.db import models
import re

email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class EmailManager(models.Manager):
    def validate(self, email):
        print("Running validation function!")
        # Checks for duplicate email
        if len(Email.objects.filter(email=email)) > 1:
            print('email already in database')
            return {
                'error': 'Email already in database'
            }
        if email_regex.match(email):
            Email.objects.create(email=email)
            return {
                'success': email
            }
        else:
            return {
                'error': 'Email is not valid!'
            }

# Create your models here.
class Email(models.Model):
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = EmailManager()
