# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

urlpatterns = patterns('data.views',
    url(r'^batteryinfo$', 'batteryinfo', name='batteryinfo'),
)