from django.db import models
from ..logRegApp.models import User
# Create your models here.
class Course(models.Model):
	user = models.ManyToManyField(User,related_name='user')
	name = models.CharField(max_length=255)
	description = models.TextField(max_length=1000)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	# courseManager = CourseManager()
	# objects=models.Manager()

# class CourseManager(models.Manager):
