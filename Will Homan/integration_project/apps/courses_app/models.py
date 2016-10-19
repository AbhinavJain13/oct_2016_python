from __future__ import unicode_literals
from django.db import models
from ..login_reg_app.models import User

class CourseManager(models.Manager):
    def add_user_to_course(self, form_data):
        course = self.get(id=form_data['course'])
        user = User.objects.get(id=form_data['user'])
        course.user.add(user)
        course.save()




class Course(models.Model):
     name = models.CharField(max_length=255)
     description = models.TextField()
     user = models.ManyToManyField('login_reg_app.User', related_name='courses')
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)

     objects = CourseManager()
