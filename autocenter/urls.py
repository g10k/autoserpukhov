# -*- encoding: utf-8 -*-
__author__ = 'Сергей'

from django.conf.urls import patterns, include, url

urlpatterns = patterns("autocenter.views",
    url(r'^$',"places",name="places"),
    url(r'^(?P<pk>\d+)/$','place',name='place')
)
