# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include

from django_social_photostream.urls import urlpatterns as django_social_photostream_urls

urlpatterns = [
    url(r'^', include(django_social_photostream_urls, namespace='django_social_photostream')),
]
