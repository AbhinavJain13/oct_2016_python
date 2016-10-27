from django.conf.urls import url,include
from . import views

# routes - - - - - - - - - - - - -

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^ninjas$',views.show_all,name='show'),
    url(r'^ninjas/(?P<ninja_color>\w+)$',views.show,name='ninjacolor'),
    url(r'^.*$', views.catchall)
]
