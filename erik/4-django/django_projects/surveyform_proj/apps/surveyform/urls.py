from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^survey_process$',views.survey_process),
    url(r'^result$',views.survey_result),
    url(r'^reset$',views.reset)
]
