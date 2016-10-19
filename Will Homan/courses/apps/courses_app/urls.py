from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^courses/destroy/(?P<id>\d+)$', views.destroy),
    url(r'^destroy/yes/(?P<id>\d+)$', views.destroy_yes),
    url(r'^add$', views.add),
    ]
