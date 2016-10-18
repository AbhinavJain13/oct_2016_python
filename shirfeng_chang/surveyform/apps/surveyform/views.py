from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'surveyform/index.html')

def process(request):
    request.session["name"] = request.POST["name"],
    request.session["loc"] = request.POST["loc"],
    request.session["lang"] = request.POST["lang"],
    request.session["comment"] = request.POST["comment"]
    return redirect('/result')

def display(request):
    return render(request, 'surveyform/results.html')
