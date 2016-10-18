from django.shortcuts import render
from django.shortcuts import render, redirect, HttpResponse
import time
import random
import string

def index(request):
    if 'balance' not in request.session:
        request.session['balance'] = 0
    if "activities" not in request.session:
        request.session['activities'] = ""
    return render(request,'ninjaGoldApp/index.html')

def process_money(request):
    tmp=0
    btn = request.POST.get('button', '')
    if btn=="farm":
         tmp=random.randint(10,20)
         request.session['balance'] += tmp
         request.session['activities'] += "<p class='green'>Earned "+str(tmp)+" golds from the farm! ("+str(time.strftime("%Y/%m/%d %I:%M %p")).lower()+")</p>"
    elif btn=="cave":
         tmp=random.randint(5,10)
         request.session['balance'] +=tmp
         request.session['activities'] += "<p class='green'>Earned "+str(tmp)+" golds from the farm! ("+str(time.strftime("%Y/%m/%d %I:%M %p")).lower()+")</p>"
    elif btn=="house":
         tmp=random.randint(2,5)
         request.session['balance'] +=tmp
         request.session['activities'] += "<p class='green'>Earned "+str(tmp)+" golds from the farm! ("+str(time.strftime("%Y/%m/%d %I:%M %p")).lower()+")</p>"
    elif btn=="casino":
         tmp=random.randint(-50,50)
         request.session['balance'] +=tmp
         if (tmp>0):
             request.session['activities'] += "<p class='green'>Earned "+str(tmp)+" golds from the farm! ("+str(time.strftime("%Y/%m/%d %I:%M %p")).lower()+")</p>"
         else:
            request.session['activities'] += "<p class='red'>Entered a casino and lost "+str(-1*tmp)+" golds... Ouch.. ("+str(time.strftime("%Y/%m/%d %I:%M %p")).lower()+")</p>"
    return redirect('/')
