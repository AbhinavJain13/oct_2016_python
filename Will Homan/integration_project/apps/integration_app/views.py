from django.shortcuts import render, redirect

def index(request):
    return render(request, 'integration_app/index.html')
