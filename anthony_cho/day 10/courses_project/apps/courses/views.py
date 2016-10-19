from django.shortcuts import render, redirect
from .models import Course

# Create your views here.
def index(request):
    context = {
        'courses': Course.objects.all()
    }
    return render(request, 'courses/index.html', context)

def add_course(request):
    if request.method == 'POST':
        Course.objects.create(name=request.POST['name'], description=request.POST['description'])
        print(request.POST['name'])
        print(request.POST['description'])
        return redirect(index)
    else:
        return redirect(index)

def destroy(request, id):
    #Course.objects.get(id=id).delete()
    context = {
        'course': Course.objects.get(id=id)
    }
    return render(request, 'courses/delete.html', context)
def confirm_destroy(request, id):
    Course.objects.get(id=id).delete()
    return redirect(index)
