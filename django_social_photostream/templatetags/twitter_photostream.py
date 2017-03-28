import requests
from django import template
from django_social_photostream import app_settings
from django.urls import reverse

register = template.Library()
URL_GRAB = app_settings.TWITTER_BASE_URL + reverse('get-posts')

@register.inclusion_tag('django_social_photostream/twitter_photos.html', takes_context=True)
def twitter_photostream(context, tags, app_id=app_settings.TWITTER_APP_ID, count=None, order_by=None):
    """
    {% twitter_photostream app_id=1 tags='testtag, anothertag' %}
    """
    params = {}
    tags = [element.lower() for element in tags.split(', ')]
    params['tags'] = tags
    params['count'] = str(count)
    params['order_by'] = str(order_by)
    local_url = URL_GRAB + str(app_id)
    data = requests.get(local_url, params=params)
    request = context['request']
    MEDIA_URL = app_settings.MEDIA_URL
    return {'photos': data.json, 'request': request, 'media_url': MEDIA_URL}