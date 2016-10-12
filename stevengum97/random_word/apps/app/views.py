from django.shortcuts import render, HttpResponse, redirect
import string
from random import choice   ##this works as oppsed to import random, then implementation of random.choice

def word_generator(size=14, chars=string.ascii_uppercase + string.digits):
    return ''.join(choice(chars) for i in range(size))

# Create your views here.
def index(request):
    if 'attempt_count' not in request.session:
        request.session['attempt_count'] = 1
    return render(request, 'index.html')



def random(request):
    print request.method
    if request.method == "POST":
        # if request.session['attempt_count'] == None:
        #     request.session['attempt_count'] = 1
        request.session['attempt_count'] += 1
        request.session['random_word'] = word_generator()
        # request.session['random_word'] = ''.join(choice(string.ascii_uppercase + string.digits) for i in range(14))


    return redirect('/')

def reset(request):
    del request.session['attempt_count']
    del request.session['random_word']
    return redirect('/')
