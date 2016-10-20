#  From inside apps/yourAppName/urls.py
from django.conf.urls import url
from . import views
  # def method_to_run(request):
urlpatterns = [
    #   url(r'^$', method_to_run)
        url(r'^$', views.index, name="index"),
        url(r"^coursesAdd/$", views.coursesAdd, name="coursesAdd"),
        url(r"^coursesDestroy/(?P<id>\d+)/$", views.coursesDestroy, name="coursesDestroy"),
        url(r"^coursesDelete/$", views.coursesDelete, name="coursesDelete"),
        url(r"^users_courses/$", views.users_courses, name="users_courses"),
        # url(r"^users_courses_add/$", views.users_courses_add, name="users_courses_add"),
        # url(r'^reset$', views.reset, name="reset")
  ]
