# -*- coding: utf-8 -*-
from models import Config

def get_site_config(request):
	try:
		return Config.objects.get(site__domain=request.get_host())
	except Exception:
		print(u'Конфигурация сайта не создана.')
		return Config.objects.get(site__domain="example.com")
