from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'^login$',views.login,name='login'),
    url(r'^logout$',views.logout,name='logout'),
    url(r'^add_course$',views.add_course,name='addcourse'),
    url(r'^users_courses$',views.users_courses,name='usercourses'),
    url(r'^course/(?P<id>\d+)$',views.course,name='show'),
    url(r'^course/(?P<id>\d+)/delete$',views.delete_course,name='delete'),
    url(r'^add_comment/(?P<id>\d+)$',views.add_comment,name='addcomment'),
]
