from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^ninjas$', views.ninjas),
    url(r'^$', views.index),
    url(r'^ninjas/(?P<color>red|blue|orange|purple)$', views.colors),
    url(r'^', views.not_april)
]


#{3,4,6}

#red|blue|orange|purple
