from django.shortcuts import render, redirect, HttpResponse

def index(request):
    return render(request,'survey/index.html')

def submit(request):
    if 'count' not in request.session:
        request.session['count']=0
    request.session['count']+=1
    if request.POST:
        request.session['first']=request.POST['name']
        request.session['dojo']=request.POST['location']
        request.session['lang']=request.POST['lang']
        request.session['comments']=request.POST['comment']
        return render(request, 'survey/submitted.html')
    else:
        return redirect('/')
def clear(request):
    temp=request.session['count']
    request.session.flush()
    request.session['count']=temp
    return redirect('/')

# Create your views here.
