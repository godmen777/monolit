"""monolit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include, patterns
from django.contrib import admin
from django.conf import settings
# flatblocks edit
from flatblocks.views import edit
from django.contrib.auth.decorators import login_required
# Accounts
from authentication.models import Account
# REST API
from rest_framework import routers, serializers, viewsets
from restapi.views import *
router = routers.DefaultRouter()
router.register(r'accounts', AccountsViewSet)
# GraphQL
from django.views.decorators.csrf import csrf_exempt
from graphene.contrib.django.views import GraphQLView

from core.schema import schema


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^graphql', csrf_exempt(GraphQLView.as_view(schema=schema))),
    url(r'^graphiql', include('django_graphiql.urls')),
    
    url(r'^api/', include(router.urls)),
    url(r'^flatblocks/(?P<pk>\d+)/edit/$', login_required(edit), name='flatblocks-edit'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^', include('core.urls')),
    url(r'^', include('authentication.urls')),
    url(r'^', include('configs.urls')),
    url(r'^', include('siteprojects.urls')),
    # url(r'^graphql', csrf_exempt(GraphQLView.as_view(schema=schema))),
]


if settings.DEBUG:
    urlpatterns += patterns('',
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_ROOT}),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
        )
