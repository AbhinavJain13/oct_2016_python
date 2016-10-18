from django.shortcuts import render, redirect, HttpResponse
import time
import random
import string

# def randomword(length):
#     return ''.join(random.choice(string.hexdigits) for i in range(length))

# Create your views here.
def index(request):
    return render(request,'disappearingNinjas/index.html')

def ninjas(request):
    if 'images' in request.session:
        request.session.clear()
    request.session['images'] = ["donatello.jpg","leonardo.jpg","michelangelo.jpg","raphael.jpg"]
    return render(request,'disappearingNinjas/ninjas.html')

def path(request, path):
    def f(x):
        return {
            'blue': 'leonardo.jpg',
            'orange': 'michelangelo.jpg',
            'red': 'raphael.jpg',
            'purple': 'donatello.jpg'
        }.get(x, 'notapril.jpg')
    request.session['images'] = [f(path)]
    return render(request,'disappearingNinjas/ninjas.html')
