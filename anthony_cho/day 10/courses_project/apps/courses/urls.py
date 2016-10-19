from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add$', views.add_course),
    url(r'^courses/destroy/(?P<id>\d+)$', views.destroy),
    url(r'^courses/confirm/(?P<id>\d+)$', views.confirm_destroy)
]
