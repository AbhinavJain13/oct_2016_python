from django.shortcuts import render, redirect
import random, datetime

# Create your views here.
def index(request):
	if not 'gains' in request.session:
		request.session['gains'] = 0
		request.session['activity'] = []
	return render(request, 'ninjagold/index.html')

def process(request):
	place = {
		'farm':(10,20),
		'cave':(5,10),
		'house':(2,5),
		'casino':(-50,50)
	}

	###Use dictionary of buildings and their earning ranges to generate a gold value
	request.session['gold'] = random.randrange(place[request.POST["building"]][0],place[request.POST["building"]][1])

	###Gold earned message appended to activity array
	if request.session['gold'] >= 0:
		request.session['activity'].append("Earned " + str(request.session['gold']) + " gold from the  " + request.POST['building'] + "! " + str(datetime.datetime.now()))
	else:
		request.session['activity'].append("Entered casino and lost " + str(request.session['gold']) + " gold... Ouch. " + str(datetime.datetime.now()))
	request.session['gains']+= request.session['gold']
	return redirect('/')
