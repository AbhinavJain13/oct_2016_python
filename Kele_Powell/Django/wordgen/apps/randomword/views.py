from django.shortcuts import render, HttpResponse, redirect
import random
import string

# Create your views here.
def index(request):
    if 'count' not in request.session:
        request.session['count']=0
    request.session['count']+=1

    context={
    'count':request.session['count']
    }

    return render(request, 'randomword/index.html',context)

def random_num(request):
        request.session['pizza']= ''.join(random.choice(string.lowercase+string.uppercase)for i in range(8))
        return redirect('/')

def clear(request):
    request.session['count']=0
    return redirect('/')
