from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add_post/$',views.add_post),
    url(r'^add_comment/(?P<id>\d+)$',views.add_comment),


]
