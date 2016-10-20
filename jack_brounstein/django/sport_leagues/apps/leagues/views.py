from django.shortcuts import render, redirect
from django.db.models import Count
from .models import League, Team, Player

# Create your views here.
def index(request):
	context = {
		"yankees": Player.objects.filter(teams__team_name="Yankees").filter(name__lt="J"),
		"big_teams": Team.objects.annotate(num_players=Count("players")).filter(num_players__gt=2),
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
	this_team = Team.objects.get(id=request.POST["team_id"])
	this_player = Player.objects.get(id=request.POST["player_id"])

	this_team.players.add(this_player)

	return redirect("index")

def remove_player_from_team(request, team_id, player_id):
	this_team = Team.objects.get(id=team_id)
	this_player = Player.objects.get(id=player_id)

	this_player.teams.remove(this_team)

	return redirect("index")