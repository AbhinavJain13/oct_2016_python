from django.shortcuts import render, HttpResponse,redirect
from .models import User
import bcrypt
from django.core.urlresolvers import reverse

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
    # return render(request,'loginreg/index.html',context)
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
            return redirect(reverse('user:index'))
        else:
            errors = u.get('errors')
            context= {
                'errors': errors
            }
            # return render(request,'loginreg/index.html',context)
            return redirect(reverse('user:index'),kwargs={context:context})
    else:
         return redirect(reverse('user:index'))

# /logout
# Logout a User
def logout(request):
    print('*'*20)
    print('LOGIN')
    print('*'*20)
    del request.session['user_id']
    return redirect(reverse('user:index'))

# /login
# Log in a User
def login(request):
    print('*'*20)
    print('LOGIN')
    print('*'*20)
    u = User.objects.login(request.POST['email'],request.POST['password'])
    print('LOGIN GOT AN ANSWER BACK',u)

    if 'self' in u:
        print('LOGGING IN USER!!')
        new_user = u.get('self')
        request.session['user_id'] = new_user.id
        request.session['first_name'] = new_user.first_name
        return redirect(reverse('user:index'))
    else:
        print('LOG-IN ERRORRRORRS!')
        errors = {'login':'Cannot Login!'}
        context= {
            'errors': errors
        }
        return render(request,'loginreg/index.html',context)
