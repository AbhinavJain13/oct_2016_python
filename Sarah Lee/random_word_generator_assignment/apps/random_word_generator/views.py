from django.shortcuts import render, redirect
from random_words import RandomWords
rw = RandomWords()

# Create your views here.
def index(request):
    if 'count' in request.session:
        request.session['count'] += 1
    else:
        request.session['count'] = 1
    print request.session['count']
    return render(request, 'random_word_generator/page.html')

def show(request):
    if request.method == "POST":
        print(request.POST)
        word = rw.random_word()
        request.session['word'] = word
        return redirect('/')

# def count(self):
#     if request.method == "POST":
#         request.session['count'] = self.count = self.count + 1
#     return redirect('/')
