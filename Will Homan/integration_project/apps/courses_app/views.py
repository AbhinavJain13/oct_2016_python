from django.shortcuts import render, redirect, HttpResponse
from django.core.urlresolvers import reverse
from .models import Course
from ..login_reg_app.models import User
from django.db.models import Count

def index(request):
    context = {
        "courses": Course.objects.all(),
    }
    return render(request, 'courses_app/index.html', context)

def add(request):
    if request.method == 'POST':
        course_name = request.POST['name']
        course_description = request.POST['description']
        Course.objects.create(name=course_name, description = course_description)
        return redirect(reverse('courses:index'))

def destroy(request, id):
    context = {
        "course": Course.objects.get(id = id)
        }
    return render(request, 'courses_app/delete.html', context)

def destroy_yes(request, id):
    Course.objects.get(id=id).delete()
    return redirect(reverse('courses:index'))

def user_courses(request):
    if request.method == 'POST':
        Course.objects.add_user_to_course(request.POST)
        return redirect(reverse('courses:user_course'))
    else:
        context = {
        'users' : User.objects.all(),
        'courses' : Course.objects.annotate(students=Count('user')),
    }
    return render(request, 'courses_app/users_courses.html', context)
