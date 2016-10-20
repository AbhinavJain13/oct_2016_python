from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class EmailManager(models.Manager):
    def validate(self, postData):
        response=""
        # response = {"state":"", "id":""}
        if (postData['email']):
            print (postData['email'])
            print ("Running an email validation function!")
            if (EMAIL_REGEX.match(postData['email'])):
                print ("Valid!")
                # response['state']=True
                # response['id']=Course.objects.create(email=postData['email'])
                # response=Course.objects.create(email=postData['email'])
                # return response
                return Email.emailManager.create(email=postData['email'])
                # pass
            else:
                print ("NOT valid!")
                # pass
        else:
            print ("Nothing passed in!")
            # pass
class Email(models.Model):
      email = models.CharField(max_length=255)
      created_at = models.DateTimeField(auto_now_add = True)
      updated_at = models.DateTimeField(auto_now = True)
      emailManager = EmailManager()
      objects=models.Manager()
