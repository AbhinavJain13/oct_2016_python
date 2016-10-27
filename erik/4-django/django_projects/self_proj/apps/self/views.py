from django.shortcuts import render,HttpResponse,redirect
from django.core.urlresolvers import reverse

from .models import Users, Friendships

# Create your views here.
def index(request):

    context = {
        "users": Users.objects.all,
        "friendships": Friendships.objects.all
    }
    return render(request,'self/index.html',context)

def create_user(request):
    u = Users.objects.create(name=request.POST['name'])
    print('CREATED: ',u)
    return redirect('/')

def make_friends(request):
    this_user = Users.objects.get(id=request.POST['user1'])
    this_friend = Users.objects.get(id=request.POST['user2'])
    f = Friendships.objects.create(user=this_user,friend=this_friend)
    print('CREATED: ',f)
    return redirect('/')
