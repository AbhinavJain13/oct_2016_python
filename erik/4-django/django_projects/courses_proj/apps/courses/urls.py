from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$',views.login),
    url(r'^logout$',views.logout),
    url(r'^add_course$',views.add_course),
    url(r'^course/(?P<id>\d+)$',views.course),
    url(r'^course/(?P<id>\d+)/delete$',views.delete_course),
    url(r'^add_comment/(?P<id>\d+)$',views.add_comment),
]
