from django.shortcuts import render, HttpResponse, redirect

def index(request):
    if 'submit_count' not in request.session:
        request.session['submit_count'] = 0
        # request.session['full_name'] = "1"
        # request.session['location'] = "2"
        # request.session['fav_lang'] = "3"
        # request.session['comment'] = "4"
    return render(request, 'survey_form/index.html')

def request(request):
    if request.method == "POST":
        request.session['submit_count'] += 1
        request.session['full_name'] = request.POST['full_name']
        request.session['location'] = request.POST['location']
        request.session['fav_lang'] = request.POST['fav_lang']
        request.session['comment'] = request.POST['comment']
    return render(request, 'survey_form/result.html')

def reset(request):
    if request.method == "POST":
        del request.session['submit_count']
    return redirect('/')

def go_back(request):
    # if request.method == "POST":
    #     if request.session['submit_count'] > 0:
    #         del request.session['full_name']
    #         del request.session['location']
    #         del request.session['fav_lang']
    #         del request.session['comment']
    return redirect('/')
