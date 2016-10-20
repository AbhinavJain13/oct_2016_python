from __future__ import unicode_literals
from django.db import models
import re, bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# CAP_REGEX = re.compile(r'^(?=.*[0-9]+.*)(?=.*[A-Z]+.*)[a-zA-Z0-9.+_-]+$')

# Create your models here.
class UserManager(models.Manager):
    def validateLogin(self, postData):
        errors={}
        user = User.userManager.filter(email=postData['email'])
        if (user):
            print (user)
            print (user[0])
            if (bcrypt.hashpw(postData['password'].encode(), user[0].password.encode()) == user[0].password.encode()):
                return {'user':user[0]}
            else:
                errors['email_pass']="Either email or password is incorrect!"
                # return {'errors':"Either email or password is incorrect!"}
                return {'errors':errors}
        else:
            errors['email_pass']="Either email or password is incorrect!"
            # return {'errors':"Either email or password is incorrect!"}
            return {'errors':errors}
            # return {'errors':"Either email or password is incorrect!"}
    def register(self, postData):
        errors={}
        if (len(postData['first_name']) < 2 or re.search('\d+', postData['first_name'])):
            errors['first_name']="First name must be at least 2 characters long and can't contain any numbers!"
        if (len(postData['last_name']) < 2 or re.search('\d+', postData['first_name'])):
            errors['last_name']="Last name must be at least 2 characters long and can't contain any numbers!"
        if (not EMAIL_REGEX.match(postData['email'])):
            errors['email_val']="Email not valid!"
        user = User.userManager.filter(email=postData['email'])
        if (user):
            errors['email_reg']="This email has already been registered!"
        if (len(postData['password']) < 8):
            errors['password']="Password must be at least 8 characters long"
        # if (not CAP_REGEX.match(postData['password'])):
        #     errors.append("Password must contain ay least 1 uppercase letter and 1 numeric value")
        if (postData['confirm_password'] != postData['password']):
            errors['password_conf']="Confirm Password doesn't match the Password!"
        if (errors):
            return {'errors':errors}
        hashedPass=bcrypt.hashpw(postData['password'].encode(),bcrypt.gensalt())
        user=User.userManager.create(first_name=postData['first_name'], last_name=postData['last_name'], email=postData['email'], password=hashedPass)
        return {'user':user}

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    userManager = UserManager()
    objects=models.Manager()
