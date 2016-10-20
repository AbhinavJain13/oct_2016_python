from django.shortcuts import render, redirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib import messages
from .models import User
# from .models import Email
import time
import random
import string

# def randomword(length):
#     return ''.join(random.choice(string.hexdigits) for i in range(length))

# Create your views here.
def index(request):
    return render(request,'logRegApp/index.html')

def validateUser(request):
    btn = request.POST.get('button', '')
    if (btn=="btnLog"):
        print("request from btnLogin")
        response=User.userManager.validateLogin(request.POST)
    if (btn=="btnReg"):
        print("request from btnRegister")
        response=User.userManager.register(request.POST)
    if ("user" in response):
        request.session['user_id']=response['user'].id
        return redirect(reverse('logRegApp:success'))
    else:
        for error in response['errors'].values():
            messages.add_message(request, messages.ERROR, error)
        # messages.add_message(request, messages.ERROR, response['error'])
    return redirect(reverse('logRegApp:index'))

def success(request):
    context={
        "user":User.userManager.get(id=request.session['user_id'])
    }
    return render(request,'logRegApp/success.html', context)
    return redirect(reverse('logRegApp:index'))
