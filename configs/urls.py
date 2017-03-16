# -*- coding: utf-8 -*-
# !/usr/bin/env python

from django.conf.urls import url
from configs.views import subscribe_view, send_contact_form
urlpatterns = [
    url(r"^subscribe/$", subscribe_view, name="subscribe"),
    url(r"^send-contact-form/$", send_contact_form, name="send_contact_form"),
]
