from django.shortcuts import render, HttpResponse, redirect
import random
import string

def random_word():
    random_word = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(14)])
    return random_word

def index(request):
    if 'count' not in request.session:
        request.session['count'] = 0
    request.session['count']+=1
    request.session['word'] = random_word()
    return render(request, 'randomword/index.html')
    # Not using render because we haven't created any templates yet!
