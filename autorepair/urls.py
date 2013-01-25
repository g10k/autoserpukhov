# -*- encoding: utf-8 -*-
__author__ = 'Сергей'
from django.core.urlresolvers import reverse

from django.conf.urls import patterns, url
from views import autorepair,list
import views
urlpatterns = patterns("autorepair.views",
    url(r"repairs/(?P<id>\d+)/$",'autorepair',name='autorepair'),
    url(r"repairs/$","list",name='repairs'),

)
