from django.shortcuts import render,HttpResponse,redirect

from .models import User,Comment,Description,Course

# Controllers ---------------------------------

# /
# Index root
def index(request):
    print('*'*20)
    print('INDEX')
    print('*'*20)

    context = {
        'users': User.objects.all(),
        'courses': Course.objects.all(),
        'descriptions': Description.objects.all()
    }

    return render(request,'courses/index.html',context)

# /login
# Attempt to login (check for valid email)
def login(request):
    print('*'*20)
    print('LOGIN')
    print('*'*20)

    email = request.POST['email']

    if User.objects.validate(email=email):
        u = User.objects.login(email)
        # set session to login user
        request.session['logged_in'] = u.id
        print('*'*20)
        print("LOGGED IN: ",request.session['logged_in'])
        print('*'*20)
        return redirect('/')
    else:
        print('*'*20)
        print("USER NOT LOGGED IN: ")
        print('*'*20)
        return redirect('/')

def logout(request,id):
    User.objects.logout(id)


# /add_course
# Create a course
def add_course(request):
    print('*'*20)
    print('ADD COURSE')
    print('*'*20)
    # need User instance
    usr = User.objects.get(id=request.session['logged_in'])
    # create the course with a User, and return a course to be used to create a description
    course = Course.objects.create(name=request.POST['course_name'],user=usr)
    print('NEW COURSE: ',course)
    # create the description, use the returned instance
    desc = Description.objects.create(description=request.POST['course_description'],user=usr,course=course)
    print('NEW DESCRIPTION: ',desc)

    return redirect('/')

# /course/<id>
# Show a course by ID
def course(request):
    print('*'*20)
    print('SHOW COURSE')
    print('*'*20)

    return redirect('/')



# /course/<id>/delete
# Delete a course by ID
def delete_course(request):
    print('*'*20)
    print('DELETE COURSE')
    print('*'*20)

    return redirect('/')


# /add_comment/<id>
# Create a comment by course ID
def add_comment(request):
    print('*'*20)
    print('ADD COMMENT')
    print('*'*20)

    return redirect('/')

def logout(request):
    print('*'*20)
    print('LOGOUT')
    print('*'*20)

    del request.session['logged_in']
    return redirect('/')
