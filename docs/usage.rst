=====
Usage
=====

To use Django social photostream in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_social_photostream.apps.DjangoSocialPhotostreamConfig',
        ...
    )

Add Django social photostream's URL patterns:

.. code-block:: python

    from django_social_photostream import urls as django_social_photostream_urls


    urlpatterns = [
        ...
        url(r'^', include(django_social_photostream_urls)),
        ...
    ]
