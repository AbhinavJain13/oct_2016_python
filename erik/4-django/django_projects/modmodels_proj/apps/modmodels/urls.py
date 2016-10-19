from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add_message/$',views.create_message),
    url(r'^add_comment/$',views.create_comment),
    url(r'^add_user/$',views.create_user),
    url(r'^login/$',views.login),
    url(r'^reset/$',views.reset)

    # url(r'^.*$', views.catchall)

]
