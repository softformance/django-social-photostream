import requests
from django import template
from django_social_photostream import app_settings
from django.urls import reverse

register = template.Library()

FACEBOOK_URL_GRAB = app_settings.FACEBOOK_BASE_URL + reverse('facebook-feed:get-posts')
TWITTER_URL_GRAB = app_settings.TWITTER_BASE_URL + reverse('twitter-feed:get-posts')
INSTAGRAM_URL_GRAB = app_settings.INSTAGRAM_BASE_URL + reverse('instagram-feed:get-posts')
list_of_url = [FACEBOOK_URL_GRAB, TWITTER_URL_GRAB, INSTAGRAM_URL_GRAB]

@register.inclusion_tag('django_social_photostream/mixed_social_photos.html', takes_context=True)
def mixed_photostream(context, tags, app_id=1, count=None, order_by=None):
    """
    {% mixed_photostream app_id=1 tags='testtag, anothertag' %}
    """
    params = {}
    tags = [element.lower() for element in tags.split(', ')]
    params['tags'] = tags
    params['count'] = str(count)
    params['order_by'] = str(order_by)
    # initialize final data to response
    data = {}
    for url in list_of_url:
        local_url = url + str(app_id)
        url_data = requests.get(local_url, params=params).json()
        data[url_data['from_site']] = url_data
    request = context['request']
    MEDIA_URL = app_settings.MEDIA_URL
    return {'data': data, 'request': request, 'media_url': MEDIA_URL}