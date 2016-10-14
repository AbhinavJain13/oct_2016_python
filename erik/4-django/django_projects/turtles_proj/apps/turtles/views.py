from django.shortcuts import render, HttpResponse, redirect

# Controllers ------------------------------------

# / Root
def index(request):
    context = {
        "show_ninjas": 0
    }
    return render(request,'turtles/index.html',context)

# /ninjas
def show_all(request):
    context = {
        "show_ninjas": 1,
        "ninja_color": "all"
    }

    return render(request,'turtles/index.html',context)

# /ninjas/<ninja_color>
def show(request,ninja_color):
    colors = ['blue','red','orange','purple']
    if ninja_color not in colors:
        ninja_color = 'hacker'
    context = {
        "show_ninjas": 1,
        "ninja_color": ninja_color
    }
    return render(request,'turtles/index.html',context)
