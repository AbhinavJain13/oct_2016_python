from django.shortcuts import render, redirect, HttpResponse
import random
import datetime

def index(request):
    if 'gold' not in request.session:
        request.session['gold']=0
    if 'log' not in request.session:
        request.session['log']=[]
    return render(request, 'gold/index.html')

def add_gold(request,build):
    buildings={
    'farm':(10,20),
    'cave':(5,10),
    'house':(2,5),
    'casino':(-50,50),
    }
    for building in buildings:
        if build == building:
            gold=random.randint(buildings[build][0],buildings[build][1])
            request.session['gold']+=gold
    messages={
     "plus":{'key':'Hooray!, you earned {} gold at the {}. ({})'.format(gold, build,datetime.datetime.now().strftime("%F %r")),'class':'green'},
    'even':{'key':"Well...At least you didn't lose any gold.... ({})".format(datetime.datetime.now().strftime("%F %r")),'class':'black'},
    'neg':{'key':'Oh no! you lost {} gold at the {}. ({})'.format(gold, build,datetime.datetime.now().strftime("%F %r")),'class':'red'},
    }

    if gold>0:
        request.session['log'].append(messages['plus'])
    elif gold==0:
        request.session['log'].append(messages['even'])
    else:
        request.session['log'].append(messages['neg'])

    return redirect('/')

def clear(request):
    request.session.flush()
    return redirect('/')

# Create your views here.
