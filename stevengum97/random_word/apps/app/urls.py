from django.conf.urls import url
# from
from . import views
# from views import index, random

urlpatterns = [
    url(r'^$', views.index),
    url(r'^random$', views.random),
    url(r'^reset$', views.reset)
]
