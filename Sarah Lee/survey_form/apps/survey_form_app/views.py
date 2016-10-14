from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return render(request, 'survey_form_app/page.html')

def process(request):
    if request.method == "POST":
        print(request.POST)
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']
    if 'count' in request.session:
        request.session['count'] += 1
    else:
        request.session['count'] = 1
    print request.session['count']
    return redirect('/result')
    # return render(request, 'survey_form_app/result.html')
#
def result(request):
    if request.method == "POST":
        return redirect('/')
    return render(request, 'survey_form_app/result.html')
