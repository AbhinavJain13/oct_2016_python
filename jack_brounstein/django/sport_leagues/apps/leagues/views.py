from django.shortcuts import render, redirect
from .models import League, Team, Player

# Create your views here.
def index(request):
	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
	}
	return render(request, "leagues/index.html", context)

def show_team(request, team_id):
	return render(request, "leagues/show_team.html")

def show_player(request, player_id):
	return render(request, "leagues/show_player.html")

def create_league(request):
	if request.method=="POST":
		League.objects.create(name=request.POST["name"], sport=request.POST["sport"])
	return redirect("index")

def create_team(request):
	if request.method=="POST":
		league = League.objects.get(id=request.POST["league_id"])
		Team.objects.create(city=request.POST["city"], team_name=request.POST["team_name"], league=league)
	return redirect("index")

def create_player(request):
	if request.method=="POST":
		Player.objects.create(name=request.POST["name"])
	return redirect("index")

def add_player_to_team(request):
	return redirect("index")