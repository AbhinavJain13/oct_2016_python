from django.shortcuts import render, redirect
import random
import string

# Create your views here.
def index(request):
	if not 'count' in request.session:
		request.session['count'] = 1
		request.session['random'] = ""
	return render(request,'randomword/index.html')

def generate(request):
	request.session['count'] += 1
	request.session['rand'] = ''.join(random.sample(string.ascii_uppercase + string.digits, 14))
	return redirect('/')
