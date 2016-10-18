from django.shortcuts import render

# Create your views here.
def index(request):
	name = "Jack"
	another_dict = {"Hey": "Buddy"}
	context = {
		"name": name,
		"key": "value",
		"number": 15, 
		"dict": another_dict
	}
	return render(request, "first_app/index.html", context)

def second(request):
	return render(request, "first_app/second.html")