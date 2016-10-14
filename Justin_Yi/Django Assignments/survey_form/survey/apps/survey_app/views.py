from django.shortcuts import render, HttpResponse, redirect


# Create your views here.
def index(request):
    return render(request,'survey_app/index.html')

def register(request):
    if 'count' in request.session:
        request.session['count'] += 1
    else:
        request.session['count'] = 1

    if request.method == 'POST':
        request.session.name = request.POST['name']
        request.session.place = request.POST['place']
        request.session.language = request.POST['language']
        request.session.comment = request.POST['comment']
    return render(request, "survey_app/result.html")
