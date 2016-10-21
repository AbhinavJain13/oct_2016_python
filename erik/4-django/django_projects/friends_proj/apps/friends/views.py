from django.shortcuts import render,redirect,HttpResponse
from .models import Blogs,Comments,User

# Controllers ------------------
def index(request):
    print('*'*20)
    print('INDEX')
    print('*'*20)

    # print("Running index method, calling out to User.")
    # user = User.objects.login("speros@codingdojo.com","Speros")
    #
    # print(type(user))
    # if 'error' in user:
    #   pass
    # if 'theuser' in user:
    #   pass
    # return HttpResponse(user)



    context = {
        "blogs": Blogs.objects.all()
    }
    print(context)
    return render(request,'friends/index.html',context)

def add_post(request):
    print('*'*20)
    print('ADD POST')
    print('*'*20)
    Blogs.objects.create(title=request.POST['title'],post=request.POST['post'])
    return redirect('/')

def add_comment(request,id):
    print('*'*20)
    print('ADD COMMENT')
    print('*'*20)
    b = Blogs.objects.get(id=id)
    print('got b to make a comment',b)
    Comments.objects.create(comment=request.POST['comment'],blog=b)
    return redirect('/')
