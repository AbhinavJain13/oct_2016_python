from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^courses/destroy/(?P<id>\d+)$', views.destroy, name='destroy'),
    url(r'^destroy/yes/(?P<id>\d+)$', views.destroy_yes, name='delete'),
    url(r'^add$', views.add, name='add'),
    url(r'^users_courses$', views.user_courses, name='user_course'),
    ]
