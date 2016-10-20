from django.shortcuts import render,HttpResponse,redirect
from django.core.urlresolvers import reverse
from ..loginreg.models import User

from .models import CUser,Comment,Description,Course

# Controllers ---------------------------------

# /
# Index root
def index(request):
    print('*'*20)
    print('INDEX')
    print('*'*20)

    context = {
        'users': CUser.objects.all(),
        'courses': Course.objects.order_by('-id'),
        'descriptions': Description.objects.all()
    }
    return render(request,'courses/index.html',context)

def users_courses(request):
    print ('USERS COURSES --------------')
    if request.method == 'POST':
        print('ITS A POST!!',request.POST)
        # this_user = User.objects.get(...)
        # this_course = Course.objects.get(...)
        # this_course.course_user.add(this_user)
        u = User.objects.get(email=request.POST['users'])
        print('REGISER USER: ',u)
        c = Course.objects.get(id=request.POST['course'])
        print('INTO THIS COURSE ',c)
        c.course_user.add(u)
        print('wellll????????')
        return render(request,'courses/users_courses.html')
    else:
        print('ITS A GET!!')
        context = {
            'users': User.objects.all(),
            'courses': Course.objects.order_by('-id'),
            # 'descriptions': Description.objects.all()
        }
        print('any users: ',User.objects.all())
        return render(request,'courses/users_courses.html',context)

# /login
# Attempt to login (check for valid email)
def login(request):
    print('*'*20)
    print('LOGIN')
    print('*'*20)

    # email = request.POST['email']
    if CUser.objects.validate(email=request.POST['email']):
        u = CUser.objects.login(request.POST['email'])
        request.session['logged_in'] = u.id
        print('*'*20)
        print("LOGGED IN: ",request.session['logged_in'])
        print('*'*20)
        return redirect(reverse('courses:index'))
    else:
        print('*'*20)
        print("USER NOT LOGGED IN: ")
        print('*'*20)
        return redirect(reverse('courses:index'))

def logout(request,id):
    User.objects.logout(id)

# /add_course
# Create a course
def add_course(request):
    print('*'*20)
    print('ADD COURSE')
    print('*'*20)
    # need User instance
    usr = CUser.objects.get(id=request.session['logged_in'])
    # create the course with a User, and return a course to be used to create a description
    course = Course.objects.create(name=request.POST['course_name'],user=usr)
    print('NEW COURSE: ',course)
    # create the description, use the returned instance
    desc = Description.objects.create(description=request.POST['course_description'],user=usr,course=course)
    print('NEW DESCRIPTION: ',desc)

    return redirect(reverse('courses:index'))

# /course/<id>
# Show a course by ID
def course(request):
    print('*'*20)
    print('SHOW COURSE')
    print('*'*20)

    return redirect(reverse('courses:index'))

# /course/<id>/delete
# Delete a course by ID
def delete_course(request,id):
    print('*'*20)
    print('DELETE COURSE')
    print('*'*20)
    Course.objects.filter(id=id).delete()
    return redirect(reverse('courses:index'))

# /add_comment/<id>
# Create a comment by course ID
def add_comment(request):
    # THIS IS NOT COMPLETED
    print('*'*20)
    print('ADD COMMENT')
    print('*'*20)
    return redirect(reverse('courses:index'))

def logout(request):
    print('*'*20)
    print('LOGOUT')
    print('*'*20)

    del request.session['logged_in']
    return redirect(reverse('courses:index'))
