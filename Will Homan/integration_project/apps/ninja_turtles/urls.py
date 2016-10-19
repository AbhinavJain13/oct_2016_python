from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^ninjas/$', views.ninja, name='ninja'),
    url(r'^ninjas/(?P<color>\w+)$', views.ninja_color, name='ninja_color'),
    ]
