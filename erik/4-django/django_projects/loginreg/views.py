from django.shortcuts import render, HttpResponse,redirect
from .models import User
import bcrypt

# Controllers -----------------------
# /
# Root
def index(request):
    print('*'*20)
    print('INDEX')
    print('*'*20)

    context = {
        'users' : User.objects.all()
    }
    return render(request,'loginreg/index.html',context)

# /registration
# Register a new user
def registration(request):
    print('*'*20)
    print('REGISTRATION')
    print('*'*20)

    if request.method == "POST":
        # print('post: ',request.POST)
        print('*'*20)
        print('REGISTRATION IN PROGRESS....')
        print('*'*20)
        # Use the Manager function to register the user
        u = User.objects.register(request.POST)
        if u.get('result') == True:
            new_user = u.get('user')
            # session variables cant be set in the model
            request.session['user_id'] = new_user.id
            request.session['first_name'] = new_user.first_name
            return redirect('/')
        else:
            errors = u.get('errors')
            context= {
                'errors': errors
            }
            return render(request,'loginreg/index.html',context)
    else:
        return redirect('/')

# /logout
# Logout a User
def logout(request):
    print('*'*20)
    print('LOGIN')
    print('*'*20)
    del request.session['user_id']
    return redirect('/')

# /login
# Log in a User
def login(request):
    print('*'*20)
    print('LOGIN')
    print('*'*20)
    if request.method == "POST":
        loggedin = User.objects.login(request.POST['email'],request.POST['password'])
        if loggedin:
            request.session['user_id'] = new_user.id
            request.session['first_name'] = new_user.first_name
            return redirect('/')
        else:
            errors = {'login': 'Login attempt failed!'}
            context= {
                'errors': errors
            }
            return render(request,'loginreg/index.html',context)
    else:
        return redirect('/')
