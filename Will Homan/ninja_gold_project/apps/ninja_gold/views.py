from django.shortcuts import render, redirect
import random
import string

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'activities' not in request.session:
        request.session['activities'] = []

    return render(request, 'ninja_gold/index.html')



def submit(request):
    if request.method == 'POST':

        if request.POST['building'] == "farm":
            turngold = random.randint(10,20)
        elif request.POST['building'] == "cave":
            turngold = random.randint(5,10)
        elif request.POST['building'] == 'house':
            turngold = random.randint(2,5)
        elif request.POST['building'] == 'casino':
            turngold = random.randint(-50,50)

        print('turngold is', turngold)
        print('activites is', request.session['activities'])
        if turngold < 0:
                string = "Entered a casino and lost " + str(turngold) + " golds....Ouch.","red"
                request.session['activities'].append(string)
        else:
                string = "Earned " + str(turngold) + " golds from the " + request.POST['building'],"green"
                request.session['activities'].append(string)
        request.session['gold'] += turngold
        print("session gold is ", request.session['gold'])
        print("activities is", request.session['activities'])
        return redirect('/')
    else:
        return redirect('/')
