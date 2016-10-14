from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, 'survey_app/index.html')


def process(request):
    if request.method == 'POST':
        if 'count' not in request.session:
            request.session['count'] = 0
        request.session['count']+=1
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']
        return redirect('/result')
    else:
        return redirect('/')

def result(request):
    return render(request, 'survey_app/results.html')
