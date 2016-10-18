from django.shortcuts import render, redirect

# Create your views here.
turtles = {
    'red':'disappearingninjas/raphael.jpg',
    'orange':'disappearingninjas/michelangelo.jpg',
    'blue':'disappearingninjas/leonardo.jpg',
    'purple':'disappearingninjas/donatello.jpg'
}

def index(request):
    context = {
        'message':1
    }
    return render(request, 'disappearingninjas/index.html', context)

def ninjas(request):
    context = {
        'all':1
    }
    return render(request, 'disappearingninjas/index.html', context)

def show(request, color):
    if color in turtles:
        context = {
            'image':turtles[color]
        }
    else:
        context = {
            'image':'disappearingninjas/notapril.jpg'
        }
    return render(request, 'disappearingninjas/index.html', context)
