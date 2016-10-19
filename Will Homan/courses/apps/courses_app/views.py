from django.shortcuts import render, redirect, HttpResponse
from .models import Course

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
        return redirect('/')

def destroy(request, id):
    context = {
        "course": Course.objects.get(id = id)
        }
    return render(request, 'courses_app/delete.html', context)

def destroy_yes(request, id):
    Course.objects.get(id=id).delete()
    return redirect('/')
