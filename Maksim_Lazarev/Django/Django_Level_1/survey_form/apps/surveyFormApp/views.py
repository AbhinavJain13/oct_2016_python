from django.shortcuts import render, redirect, HttpResponse
import time
import random
import string

# Create your views here.
def index(request):
    return render(request,'surveyFormApp/index.html')

def survey_process(request):
    request.session['name']=request.POST['name']
    request.session['location']=request.POST['location']
    request.session['language']=request.POST['language']
    request.session['comment']=request.POST['comment']
    if 'count' in request.session:
        request.session['count']+=1
    else:
        request.session['count']=1
    print (request.session['count'])
    return redirect('/result')

def result(request):
    return render(request,'surveyFormApp/result.html')
