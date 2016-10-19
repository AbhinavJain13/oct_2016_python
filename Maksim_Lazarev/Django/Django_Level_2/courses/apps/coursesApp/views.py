from django.shortcuts import render, redirect, HttpResponse
from .models import Course
import time
import random
import string

# def randomword(length):
#     return ''.join(random.choice(string.hexdigits) for i in range(length))

# Create your views here.
def index(request):
    context = {
    "courses": Course.objects.all()
    }
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
    return render(request,'coursesApp/index.html', context)
    # return render(request,'coursesApp/index.html', context)

def coursesAdd(request):
    Course.objects.create(name=request.POST['courseName'], description=request.POST['courseDescription'])
    return redirect('/')

def coursesDestroy(request, id):
    context = {
    "course": Course.objects.get(id=id)
    }
    return render(request,'coursesApp/destroy.html', context)

def coursesDelete(request):
    Course.objects.get(id=request.POST['btnDelYes']).delete()
    return redirect('/')

# def reset(request):
#     request.session.clear()
#     return redirect('/')
