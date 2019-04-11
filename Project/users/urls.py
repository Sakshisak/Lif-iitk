# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.home, name='web_home'),
    url(r'^about/$', views.about, name='web_about'),
    url(r'^register/$', views.register, name='register'),
]
