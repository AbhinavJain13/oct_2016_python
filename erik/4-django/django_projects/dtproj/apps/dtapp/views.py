from django.shortcuts import render, HttpResponse,redirect

import time

def index(request):
    print(request.method)
    dt = time.asctime()
    print dt
    context = {
        "dt":dt
    }
    return render(request,'dtapp/index.html',context)

def show(request):
    print(request.method)
    context = {

    }
    return render(request,'dtapp/users.html',context)

def create(request):
    if request.method == 'POST':
        print('*'*80)
        print(request.method)
        print('*'*80)
        print(request.POST)
        print('*'*80)
        # request.session.first_name = request.POST.first_name
        request.session['first_name'] = request.POST['first_name']
        print('request.session first_name ',request.session['first_name'])
        return redirect('/')
    else:
        print('*'*80)
        print(request.method)
        print('*'*80)
        print(request.GET)
        print('*'*80)



    context = {

    }
    return render(request,'dtapp/add_users.html',context)
