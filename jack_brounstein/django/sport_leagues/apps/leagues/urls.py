from django.conf.urls import url
from . import views

urlpatterns = [
	url(r"^$", views.index, name="index"),
	url(r"^show_team/(?P<team_id>\d+)$", views.show_team, name="show_team"),
	url(r"^show_player/$(?P<player_id>\d+)", views.show_player, name="show_player"),
	url(r"^add_player_to_team/$", views.add_player_to_team, name="add_player_to_team"),
	url(r"^create_league", views.create_league, name="create_league"),
	url(r"^create_team", views.create_team, name="create_team"),
	url(r"^create_player", views.create_player, name="create_player"),
]