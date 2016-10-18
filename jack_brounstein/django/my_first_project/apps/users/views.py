from django.shortcuts import render, redirect

# Create your views here.
def index(request):
	return render(request, "users/index.html")

def show(request, name):
	context = {
		"name": name,
	}
	return render(request, "users/show.html", context)

def process(request):
	if request.method=="POST":
		return redirect("/users/"+request.POST["name"])
	else:
		return redirect("/users")