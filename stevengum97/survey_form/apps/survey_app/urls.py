from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^request$', views.request),
    # url(r'^result$', views.result),
    url(r'^go_back$', views.go_back),
    url(r'^reset$', views.reset)
]
