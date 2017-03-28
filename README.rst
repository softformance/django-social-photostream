=============================
Django social photostream
=============================

.. image:: https://badge.fury.io/py/django-social-photostream.svg
    :target: https://badge.fury.io/py/django-social-photostream

.. image:: https://travis-ci.org/DmytroLitvinov/django-social-photostream.svg?branch=master
    :target: https://travis-ci.org/DmytroLitvinov/django-social-photostream

.. image:: https://codecov.io/gh/DmytroLitvinov/django-social-photostream/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/DmytroLitvinov/django-social-photostream

Include photostream into your template with Django-social-photostream

Documentation
-------------

The full documentation is at https://django-social-photostream.readthedocs.io.

Quickstart
----------

Install Django social photostream::

    pip install django-social-photostream

Add it to your `INSTALLED_APPS`:

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

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
