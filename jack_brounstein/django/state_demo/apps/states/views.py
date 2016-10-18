from django.shortcuts import render, redirect
from .models import City, State

# Create your views here.
def index(request):
	context = {
		"states": State.objects.all(),
		"cities": City.objects.all()
	}
	return render(request, "states/index.html", context)

def show(request, state_id):
	state = State.objects.get(id=state_id)
	context = {
		"state": state,
		# "cities": City.objects.filter(state=state),
	}
	return render(request, "states/show.html", context)

def create(request):
	if request.method=="POST":
		print(request.POST)

		new_state = State()

		new_state.name = request.POST["name"]
		new_state.governor = request.POST["governor"]

		new_state.save()

	return redirect("index")

def create_city(request):
	if request.method=="POST":
		print(request.POST)

		state = State.objects.get(id=request.POST["state_id"])

		City.objects.create(name=request.POST["name"], state=state)

	return redirect("index")