# -*- coding: utf-8 -*-
from django import template
register = template.Library()
from configs.methods import get_site_config


def phone(context, request):
    return {
    	# 'configs': configs,
        'request': request,
    }
register.inclusion_tag('core/tags/phone.html', takes_context=True)(phone)


def contact_form(context, request):
    config = get_site_config(request)
    return {
        'config': config,
        'request': request,
    }
register.inclusion_tag('core/tags/contact_form.html', takes_context=True)(contact_form)


def search_tag(context, request):
    return {
    	# 'configs': configs,
        'request': request,
    }
register.inclusion_tag('core/tags/search_tag.html', takes_context=True)(search_tag)