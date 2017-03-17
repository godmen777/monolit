#-*- coding: utf-8 -*-
from django import template
from configs.models import *
from configs.forms import *
from configs.methods import get_site_config
from authentication.models import Account

register = template.Library()


def top_menu(context, request):
    config = get_site_config(request)
    return {
        'config': config,
        'request': request,
    }
register.inclusion_tag('configs/tags/top_menu.html', takes_context=True)(top_menu)


def base_menu(context, request):
    try:
        config = Config.objects.get(site__domain=request.get_host())
    except Exception:
        config = Config.objects.get(site__domain="example.com")

    return {
        'config': config,
        'user': request.user,
        'request': request,
    }
register.inclusion_tag('configs/tags/base_menu.html', takes_context=True)(base_menu)


def contact_form(context, request):
    config = get_site_config(request)
    performer_profile = config.account.performer_of_account
    form = ContactForm()
    return {
        'config': config,
        'performer_profile': performer_profile,
        'form': form,
        'request': request,
    }
register.inclusion_tag('configs/tags/contact_form.html', takes_context=True)(contact_form)



def measure_form(context, request):
    config = get_site_config(request)
    performer_profile = config.account.performer_of_account
    form = MeasureForm()
    return {
        'config': config,
        'performer_profile': performer_profile,
        'form': form,
        'request': request,
    }
register.inclusion_tag('configs/tags/measure_form', takes_context=True)(measure_form)



def contact_widget(context, request):
    config = get_site_config(request)
    performer_profile = config.account.performer_of_account
    return {
        'config': config,
        'performer_profile': performer_profile,
        'request': request,
    }
register.inclusion_tag('configs/tags/contact_widget.html', takes_context=True)(contact_widget)


def calc(context, request):
    config = get_site_config(request)
    performer_profile = config.account.performer_of_account
    return {
        'config': config,
        'performer_profile': performer_profile,
        'request': request,
    }
register.inclusion_tag('configs/tags/calc.html', takes_context=True)(calc)
