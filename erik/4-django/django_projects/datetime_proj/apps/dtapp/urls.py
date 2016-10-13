from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$',views.index),
    url(r'^users$',views.show),
    url(r'^add_user$',views.create)
]
