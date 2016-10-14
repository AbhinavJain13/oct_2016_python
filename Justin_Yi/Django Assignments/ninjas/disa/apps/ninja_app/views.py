from django.shortcuts import render

def index(request):
    return render(request,'ninja_app/main.html')

def show(request, ninja_color): # <- points to regex in urls.
    if ninja_color == 'purple':
        context ={
        'img':'ninja_app/images/donatello.jpg'
        }
    elif ninja_color == 'blue':
        context ={
        'img':'ninja_app/images/leonardo.jpg'
        }
    elif ninja_color == 'orange':
        context = {
        'img': 'ninja_app/images/michelangelo.jpg'
        }
    elif ninja_color == 'red':
        context = {
        'img' : 'ninja_app/images/raphael.jpg'
        }
    else :
        context = {
        'img' : 'ninja_app/images/notapril.jpg'
        }

    return render(request,'ninja_app/index.html', context)
