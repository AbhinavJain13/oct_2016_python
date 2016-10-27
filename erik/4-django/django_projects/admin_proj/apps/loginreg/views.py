from django.shortcuts import render, HttpResponse,redirect
import bcrypt
from django.core.urlresolvers import reverse

# MODELS TO IMPORT FROM APPS
from .models import User


# Controllers ------------------------------------------

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


# EMAIL IN THE DATABASE
def registered_email(self,email):
    try:
        u = User.objects.get(email = request.POST['email'])
        return True
    except:
        return False

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
        # Use the Manager function to do validations & register the user
        u = User.objects.register(request.POST)
        if u.get('result') == True:
            new_user = u.get('user')
            request.session['user_id'] = new_user.id
            request.session['first_name'] = new_user.first_name
            # NOTE: --> SUCCESS! REDIRECT NEW USER TO NAMED ROUTE!
            # return redirect(reverse('baseapp:show'))
            return render(request,'baseapp/index.html')
            # --> POINT TO LOGIN REG HOME
            #return redirect(reverse('user:index'))
        else:
            errors = u.get('errors')
            print('REGISTRATION ERRORS!!',errors)
            context= {
                'errors': errors
            }
            # NOTE: --> FAILURE!
            return render(request,'loginreg/index.html',context)
    else:
         return redirect(reverse('user:index'))

# /logout
# Logout a User
def logout(request):
    print('*'*20)
    print('LOG OUT')
    print('*'*20)
    try:
        del request.session['user_id']
        print('*'*10, 'Logged Out')
        # NOTE --> AFTER LOGOUT GO THIS NAMED ROUTE
        return redirect(reverse('user:index'))
    except:
        return redirect(reverse('user:index'))

# /login
# Log in a User
def login(request):
    print('*'*20)
    print('LOGIN')
    print('*'*20)
    if request.method == 'POST':
        try:
            u = User.objects.login(request.POST['email'],request.POST['password'])
            print('LOGIN GOT AN ANSWER BACK',u)
            if 'self' in u:
                print('LOGGING IN USER!!')
                new_user = u.get('self')
                print(new_user)
                request.session['user_id'] = new_user.id
                request.session['first_name'] = new_user.first_name
                # NOTE --> SUCCESS! REDIRECT THE LOGGED IN USER
                # TO FIRST APP USING ITS NAMED ROUTE
                # return redirect(reverse('user:index'))
                return redirect(reverse('baseapp:show'))
            else:
                print('LOG-IN ERROR!')
                errors = {'login':'Login Attempt Failed!'}
                context= {
                    'errors': errors
                }
                # --> FAILURE!
                return render(request,'loginreg/index.html',context)
        except:
            print('LOG-IN ERROR!')
            errors = {'login':'Login Attempt Failed!'}
            context= {
                'errors': errors
            }
            # --> FAILURE!
            return render(request,'loginreg/index.html',context)
    else:
         return redirect(reverse('user:index'))
