import os, sys

sys.path[:0] = [os.path.abspath(os.path.dirname(__file__))]

# Google App Engine imports.
from google.appengine.ext.webapp import util

# Must set this env var before importing any part of Django
# 'project' is the name of the project created with django-admin.py
os.environ['DJANGO_SETTINGS_MODULE'] = 'iovisual.settings_dev'

# Force Django to reload its settings.
from django.conf import settings
settings._target = None

import logging
import django.core.handlers.wsgi
import django.core.signals
import django.db

def log_exception(*args, **kwds):
    logging.exception('Exception in request:')

# Log errors.
django.core.signals.got_request_exception.connect(log_exception)

# Unregister the rollback event handler.
django.core.signals.got_request_exception.disconnect(django.db._rollback_on_exception)


def main():
    # Create a Django application for WSGI.
    application = django.core.handlers.wsgi.WSGIHandler()

    # Run the WSGI CGI handler with that application.
    util.run_wsgi_app(application)

if __name__ == '__main__':
    main()
