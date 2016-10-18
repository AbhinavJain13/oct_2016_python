
from django.conf.urls import url , include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^clear$', views.clear),
    url(r'^(?P<build>\w+)$', views.add_gold),
]
