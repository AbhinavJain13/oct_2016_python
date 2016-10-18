from django.shortcuts import render, redirect
import time
import random
import string

def randomword(length):
    return ''.join(random.choice(string.hexdigits) for i in range(length))

# Create your views here.
def index(request):
    if 'count' in request.session:
        request.session['count']+=1
    else:
        request.session['count']=1
    context = {
    "rndWord":randomword(14),
    "count":request.session['count']
    # "date":time.strftime("%b %d, %Y"),
    # "time":time.strftime("%I:%M %p")
    }
    return render(request,'rwg/index.html', context)

def reset(request):
    request.session.clear()
    return redirect('/')
