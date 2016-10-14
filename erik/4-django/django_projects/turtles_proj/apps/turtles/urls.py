from django.conf.urls import url,include
from . import views
# routes - - - - - - - - - - - - -

urlpatterns = [
    url(r'^$',views.index),
    url(r'^ninjas/$',views.show_all),
    url(r'ninjas/(?P<ninja_color>\w+)/$',views.show)
]
