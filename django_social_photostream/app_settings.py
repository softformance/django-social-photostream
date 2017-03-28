from django.conf import settings

#Insert here your settings const.
TWITTER_BASE_URL = getattr(settings, 'TWITTER_BASE_URL', 'http://localhost:8001')

GET_MEDIAS_COUNT = getattr(settings, 'GET_MEDIAS_COUNT', 10)

TWITTER_APP_ID = getattr(settings, 'TWIITER_APP_ID', 1)

MEDIA_URL = getattr(settings, 'MEDIA_URL')