from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^ninjas$', views.index),
    url(r'^ninjas/(?P<ninja_color>\w+)$', views.show)
]
