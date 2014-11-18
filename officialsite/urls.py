# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

urlpatterns = patterns('officialsite.views',
    url(r'^$', 'official_site', name='official_site'),
)