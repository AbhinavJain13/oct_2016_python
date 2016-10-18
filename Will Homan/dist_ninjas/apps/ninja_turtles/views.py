from django.shortcuts import render, redirect

def index(request):
    return render(request, 'ninja_turtles/index.html')

def ninja(request):
    context = {
    'color' : ""
    }
    return render(request, 'ninja_turtles/ninja.html', context)

def ninja_color(request, color):
    context = {
    'color': color
    }
    return render(request, 'ninja_turtles/ninja.html', context)
