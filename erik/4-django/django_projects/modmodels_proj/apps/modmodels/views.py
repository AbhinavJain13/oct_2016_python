from django.shortcuts import render,HttpResponse,redirect

from .models import Users,Comments,Msgs


# Controllers ------------------------------

# / goin roooooot down
def index(request):

    messages = Msgs.objects.all().order_by('-created_at')
    print('Messages: ',messages)
    print('*'*20)

    users = Users.objects.all().order_by('-created_at')
    print('Users: ',users)
    print('*'*20)

    comments = Comments.objects.all().order_by('-created_at')
    print('Comments: ',comments)
    print('*'*20)

    context = {
        'users': users,
        'msgs': messages,
        'comments': comments
    }

    return render(request,'modmodels/index.html',context)

# /add_user
# Create a new user
def create_user(request):
    if(request.method == 'POST'):
        # validation first...
        print('Create POST: ',request.POST,'*'*15)

        # then
        first_name = request.POST.get('first_name','0')
        last_name = request.POST.get('last_name','0')
        email = request.POST.get('email','0')
        password = request.POST.get('password','0')
        # print('first:',first_name)

        # returns User object
        new_user = Users.objects.create(first_name = first_name,last_name = last_name,email = email,password = password)

        print('NEW USER! ',new_user,'*'*15)
        # print('and the id: ',new_user.id)
        # login the newly created user
        request.session['current_user_id'] = new_user.id
        print('Sess: ',request.session['current_user_id'])

        return redirect('/')

# /add_message
# Create a new message
def create_message(request):
    print("CREATE MESSSAGE * !"*50)

    message = request.POST.get('message','0')
    # need a Users instance
    usr = Users.objects.get(id = request.session['current_user_id'])
    print('GOT INSTANCE',usr)
    # create the message
    new_msg = Msgs.objects.create(message=message,user_id=usr)
    return redirect('/')

# /add_comment
# Create a new comment
def create_comment(request):
    print("CREATE COMMENT * !"*50)

    comment = request.POST.get('comment','0')

    # need a Users instance
    usr = Users.objects.get(id = request.session['current_user_id'])
    print('GOT INSTANCE',usr)
    # need a Message instance
    msg = Msgs.objects.get(id = request.POST.get('message_id','0'))
    print('GOT INSTANCE',msg)
    # create a comment
    new_comment = Comments.objects.create(comment=comment,user_id=usr,message_id=msg)
    return redirect('/')

# /login
# Login a user
def login(request):
    if(request.method=='POST'):
        print('*'*20)
        print('Login POST: ',request.POST)
        print('*'*20)
        # NOTE: there are a ton of users in the db with the same email, as it was the form default
        # did this so i wouldnt have to type it all the time in dev, that's why this guery.
        # PROD: only get one: change it from .filter to .get and remove the [0] index
        user = Users.objects.filter(email = request.POST['email_login'])[0]
        print('*'*20)

        # validation...kinda of
        if( 'email_login' in request.POST):
            # check for match would usually include encryption AND A PASSWORD, but this is a mock up...
            if request.POST['email_login'] == user.email:
                request.session['current_user_id'] = user.id
                return redirect('/')
            else:
                # create an error message for password mismatch...
                print('FAILED TO LOGIN','*'*20)
                return redirect('/')
        else:
            # create an error message for invalid entry, when you figure that out....
            print('FAILED TO LOGIN-INVALID FORM ENTRY','*'*20)
            return redirect(request,'/')
    else:
        return redirect(request,'/')

# /logout
# Logout a user
def reset(request):
    del request.session['current_user_id']
    return redirect('/')
