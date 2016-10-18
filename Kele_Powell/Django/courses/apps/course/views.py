from django.shortcuts import render, redirect
from .models import Course
# Create your views here.
def index(request):
    context={
    'books':Course.objects.all(),
    }
    return render(request, 'course/index.html',context)
def process(request):
    if len(request.POST['title'])>1 and len(request.POST['info']) >1:
        Course.objects.create(name=request.POST['title'],descript=request.POST['info'])
    return redirect('/')
def delete(request,id):
    context={
    'book':Course.objects.get(id=id)
    }
    return render(request, "course/delete.html",context)
def destroy(request,id):
    Course.objects.get(id=id).delete()
    return redirect('/')
