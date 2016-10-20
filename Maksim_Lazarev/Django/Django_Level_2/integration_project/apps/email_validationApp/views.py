from django.shortcuts import render, redirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib import messages
from .models import Email
import time
import random
import string

# def randomword(length):
#     return ''.join(random.choice(string.hexdigits) for i in range(length))

# Create your views here.
def index(request):
    # if 'count' in request.session:
    #     request.session['count']+=1
    # else:
    #     request.session['count']=1
    # context = {
    # "rndWord":randomword(14),
    # "count":request.session['count']
    # # "date":time.strftime("%b %d, %Y"),
    # # "time":time.strftime("%I:%M %p")
    # }
    return render(request,'email_validationApp/index.html')

def process(request):
    response=Email.emailManager.validate(request.POST)
    if (response):
        print (response)
        print (response.email)
        messages.add_message(request, messages.SUCCESS, response.email)
        return redirect(reverse('email_validationApp:success'))
    else:
        print ("message from view: Email not valid!")
        messages.add_message(request, messages.ERROR, 'Email is not valid!')
    # messages.add_message(request, messages.ERROR, 'Nothing passed in.')
    # messages.add_message(request, messages.ERROR, 'Email is not valid.')
        return redirect(reverse('email_validationApp:index'))

def success(request):
    useremails=Email.emailManager.all()
    if (useremails):
        context = {
            "useremails":Email.emailManager.all()
        }
        return render(request,'email_validationApp/success.html', context)
    else:
        return redirect(reverse('email_validationApp:index'))

def delete(request):
    Email.emailManager.get(id=request.POST['btnDel']).delete()
    return redirect(reverse('email_validationApp:success'))
# def reset(request):
#     request.session.clear()
#     return redirect('/')
