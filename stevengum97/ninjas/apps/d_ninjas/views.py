from django.shortcuts import render, redirect

# Create your views here.

def ninjas(request):
    return render(request, 'ninjas/ninjas.html')

def index(request):
    return render(request, 'ninjas/index.html')

def colors(request, color):
    context = {
    "color" : color,
    }
    print color
    return render(request, 'ninjas/colors.html', context)

def not_april(request):
    return render(request, 'ninjas/not_april.html')
