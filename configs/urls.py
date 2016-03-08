# -*- coding: utf-8 -*-
#!/usr/bin/env python

from django.conf.urls import patterns, include, url
# from configs.views import SubscribeView

urlpatterns = patterns('configs.views',
	url(r"^subscribe$", 'subscribe_view', name="subscribe")
)
