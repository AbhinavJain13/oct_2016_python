from django.db import models

# Create your models here.
class State(models.Model):
	name = models.CharField(max_length=20)
	governor = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class City(models.Model):
	name = models.CharField(max_length=255)
	state = models.ForeignKey(State, related_name="cities")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)