from django.shortcuts import render
from django.contrib.auth.models import User

def index(request):

    if(request.method=='GET'):
        if('random_hash' in request.session):
            del request.session['random_hash']
        # generate the 'word'
        request.session['random_hash'] = User.objects.make_random_password()

        if('count' in request.session):
             request.session['count'] += 1
        else:
            request.session['count'] = 1
        return render(request,'random_hash/index.html')

    else:
        return render(request,'random_hash/index.html')
