from django.db import models

# Create your models here.
class League(models.Model):
	name = models.CharField(max_length=255)
	sport = models.CharField(max_length=40)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Team(models.Model):
	city = models.CharField(max_length=40)
	team_name = models.CharField(max_length=60)
	league = models.ForeignKey(League, related_name="teams")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Player(models.Model):
	name = models.CharField(max_length=255)
	teams = models.ManyToManyField(Team, related_name="players")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)