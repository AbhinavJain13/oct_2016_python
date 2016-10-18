from django.shortcuts import render, redirect, HttpResponse
# Create your views here.
def index(request):
    context={
    'message':"Oops no ninjas here!"
    }
    return render(request, 'ninjas/index.html', context)
def logo(request):
    context={
    'color':'yellow',
    'pic':'ninjas/imgs/logo.png',
    }

    return render(request, 'ninjas/index.html',context)
def turtles(request,color):
    message=""
    if color:
        if color=="blue":
            pic='ninjas/imgs/blue.png'
        elif color=="purple":
            pic='ninjas/imgs/purple.png'
        elif color=="orange":
            pic='ninjas/imgs/orange.png'
        elif color=="red":
            pic='ninjas/imgs/red.png'
        else:
            pic='ninjas/imgs/oogway.png'
            message="Oops! youve gone to far! you must turn back!"
    else:pic='ninjas/imgs/logo.png'

    context={
    'color':color,
    'pic':pic,
    'message':message
    }
    return render(request, 'ninjas/index.html', context)
