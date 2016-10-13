from django.shortcuts import render, redirect, HttpResponse
import random
import string

def index(request):
    if 'count' in request.session:
        request.session['count'] += 1
    else:
        request.session['count'] = 1
    context = {
    'count' : request.session['count']
    }
    return render(request, 'word_generator/index.html',context)

def create(request):
    if request.method == 'GET':
        request.session['random'] = ''.join(random.choice(string.ascii_uppercase + string.digits) for i in range(14))
        return redirect('/')
