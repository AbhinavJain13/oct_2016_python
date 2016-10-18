from django.db import models
# Create your models here.
class Course(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField(max_length=1000)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

# class Friendship(models.Model):
# 	user = models.ForeignKey(User, related_name="user_friendships")
# 	friend = models.ForeignKey(User, related_name="friend_friendships")
# 	created_at = models.DateTimeField(auto_now_add=True)
# 	updated_at = models.DateTimeField(auto_now=True)
