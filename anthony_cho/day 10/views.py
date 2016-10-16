from django.shortcuts import render, redirect
from .models import User, Friendship

# Create your views here.
def index(request):
	#users = User.objects.all()
	#users = User.objects.filter(last_name="Rodriguez")
	#users = User.objects.exclude(last_name="Rodriguez")
	#users = User.objects.filter(last_name="Rodriguez") | User.objects.filter(first_name="Daniel")
	#users = User.objects.filter(last_name="Rodriguez").exclude(first_name="Madison")
	#users = User.objects.exclude(first_name="Daniel").exclude(first_name="Michael")
	#users = User.objects.get(id=1)
	#users = User.objects.all().order_by('first_name')
	#users = User.objects.all().order_by('last_name').reverse()
	#friendships = Friendship.objects.filter(user=6)
	#friendships = Friendship.objects.filter(friend=6)
	friendships = Friendship.objects.exclude(user=4).exclude(user=5).exclude(user=6)
	context = {
		"friendships": friendships
	}
	return render(request, "friends/index.html", context)
