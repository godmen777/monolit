# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from configs.forms import SubscribeForm, ContactForm
from django.shortcuts import redirect, render_to_response

def subscribe_view(request, template_name="configs/success.html"):
	if request.method == "POST":
		form = SubscribeForm(request.POST)

		if form.is_valid():
			form.send_email(request)

	return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def send_contact_form(request, template_name="configs/success.html"):
	if request.method == "POST":
		form = ContactForm(request.POST)

		if form.is_valid():
			form.send_email(request)
			return render_to_response(template_name, locals(), context_instance=RequestContext(request))