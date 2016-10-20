from django.shortcuts import render, redirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib import messages
# from django.db.models import Count
from .models import Course
from ..logRegApp.models import User
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
    return render(request,'coursesApp/index.html', context)

def coursesAdd(request):
    Course.objects.create(name=request.POST['courseName'], description=request.POST['courseDescription'])
    # return redirect('/')
    return redirect(reverse('coursesApp:index'))

def coursesDestroy(request, id):
    context = {
    "course": Course.objects.get(id=id)
    }
    return render(request,'coursesApp/destroy.html', context)

def coursesDelete(request):
    Course.objects.get(id=request.POST['btnDelYes']).delete()
    # return redirect('/')
    return redirect(reverse('coursesApp:index'))

def users_courses(request):
    if request.method == 'POST':
        this_course = Course.objects.get(id=request.POST["Courses"])
        this_user = User.objects.get(id=request.POST["Users"])
        if (this_user in this_course.user.all()):
            # if (Course.user.get(id=request.POST["Users"])):
            print ("already enrolled")
        else:
            this_course.user.add(this_user)
            return redirect(reverse('coursesApp:users_courses'))
    else:
        context = {
        "users": User.userManager.all(),
        "courses": Course.objects.all()
        }
    return render(request,'coursesApp/users_courses.html', context)
# def users_courses(request):
#     context = {
#     "users": User.userManager.all(),
#     "courses": Course.objects.all(),
#     }
#     return render(request,'coursesApp/users_courses.html', context)
#
# def users_courses_add(request):
#     this_course = Course.objects.get(id=request.POST["Courses"])
#     this_user = User.objects.get(id=request.POST["Users"])
#     if (this_user in this_course.user.all()):
#     # if (Course.user.get(id=request.POST["Users"])):
#         print ("already enrolled")
#     else:
#         this_course.user.add(this_user)
#     return redirect(reverse('coursesApp:users_courses'))
