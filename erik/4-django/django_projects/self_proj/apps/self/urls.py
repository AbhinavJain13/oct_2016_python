from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^create_user$',views.create_user),
    url(r'^make_friends$',views.make_friends)
]
