# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 21:25:32 2017

@author: Administrator
"""

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]