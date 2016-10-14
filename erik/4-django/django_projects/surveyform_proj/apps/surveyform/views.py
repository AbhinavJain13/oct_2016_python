from django.shortcuts import render,HttpResponse,redirect


# Controllers ------------------------------------

# / Root
def index(request):

    return render(request,'surveyform/index.html')

# /survey_process
def survey_process(request):

    if(request.method=='POST'):
        print(request.POST)
        # validation
        errorCount = 0
        if(not len(request.POST['first_name']) > 1 ):
            #messages.error(request, 'Document deleted.')
            errorCount +=1
        if(not len(request.POST['location']) > 1 ):
            #messages.error(request, 'Document deleted.')
            errorCount +=1
        if(not len(request.POST['language']) > 1 ):
            #messages.error(request, 'Document deleted.')
            errorCount +=1
        # note: comment textarea is optional
        if(errorCount):
            return redirect('/')
        # visit counter
        if('counter' in request.session):
            request.session['counter'] += 1
        else:
            request.session['counter'] = 1

        request.session['data'] = request.POST

        return redirect('/result')
    else:
        return redirect('/')

# /result
def survey_result(request):
    request.session['show_form'] = 1
    return render(request,'surveyform/index.html')

# /reset
def reset(request):
    del request.session['data']['first_name']
    del request.session['data']['language']
    del request.session['data']['location']
    del request.session['data']['comment']
    request.session['show_form'] = 1
    return redirect('/')
