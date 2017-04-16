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

Install Django social photostrean from GitHub::

    virtualenv photostream
    source photostream/bin/activate
    pip install -e git+https://github.com/softformance/django-social-photostream.git#egg=django-social-photostream

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_social_photostream',
        ...
    )

Add needed constants to ``settings.py``:

.. code-block:: python

    # Twitter settings
    TWITTER_BASE_URL = 'http://www.MyWebSite.com' # in dev environments default localhost:8001
    TWITTER_APP_ID = 1 # From which Twitter app sync photos. 

    # Facebook settings
    FACEBOOK_BASE_URL = 'http://www.MyWebSite.com' # in dev environments default localhost:8001
    FACEBOOK_APP_ID = 1 # From which Facebook app sync photos. 

    # Instagram settings
    INSTAGRAM_BASE_URL = 'http://www.MyWebSite.com' # in dev environments default localhost:8001
    INSTAGRAM_APP_ID = 1 # From which Instagram app sync photos.


Features
--------

* Show the photos from your ``django-{{social-name-site}}-photo-api`` package. 

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
