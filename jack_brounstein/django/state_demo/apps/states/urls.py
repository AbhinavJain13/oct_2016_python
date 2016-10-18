from django.conf.urls import url
from . import views

urlpatterns = [
	url(r"^$", views.index, name="index"),
	url(r"^show/(?P<state_id>\d+)$", views.show, name="show"),
	url(r"^create/", views.create, name="create"),
	url(r"^create_city/", views.create_city, name="create_city"),
]