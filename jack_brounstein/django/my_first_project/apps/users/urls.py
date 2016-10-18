from django.conf.urls import url
from . import views

urlpatterns = [
	url(r"^", views.index, name="index"),
	url(r"^(?P<name>\w+)$", views.show, name="show"),
	url(r"^process$", views.process, name="process"),
]