# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 21:25:32 2017

@author: Administrator
"""

from django.conf.urls import url
from . import views

app_name = 'votes'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /votes/5/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # ex: /votes/5/results/
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    # ex: /votes/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]