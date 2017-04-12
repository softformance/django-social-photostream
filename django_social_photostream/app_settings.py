from django.conf import settings

#Insert here your settings const.
# Twitter settings
TWITTER_BASE_URL = getattr(settings, 'TWITTER_BASE_URL', 'http://localhost:8001')
TWITTER_APP_ID = getattr(settings, 'TWIITER_APP_ID', 1)

# Facebook settings
FACEBOOK_BASE_URL = getattr(settings, 'FACEBOOK_BASE_URL', 'http://localhost:8001')
FACEBOOK_APP_ID = getattr(settings, 'FACEBOOK_APP_ID', 1)


GET_MEDIAS_COUNT = getattr(settings, 'GET_MEDIAS_COUNT', 10)

MEDIA_URL = getattr(settings, 'MEDIA_URL')