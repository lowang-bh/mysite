#!/usr/bin/env python
from django.conf.urls import url

from . import views
app_name = "polls" #set the application namespace, don't take effect, should in root url
urlpatterns = [
    url(r'^$', views.index, name='index'),
    ## Examples: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    ## Examples: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    ## Examples: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
