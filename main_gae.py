import os, sys

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

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

PUBLIC_DOMAINS = ('www.iovisual.com', 'localhost:8080')

def main():
    # Create a Django application for WSGI.
    _application = django.core.handlers.wsgi.WSGIHandler()
    if (os.environ.get('HTTP_HOST') or os.environ['SERVER_NAME'] 
        + ':' + os.environ['SERVER_PORT']) in PUBLIC_DOMAINS:
        def application(environ, start_response):
            from google.appengine.api import users
            if users.is_current_user_admin() or os.environ.get('PATH_INFO') == '/login':
                return _application(environ, start_response)

            start_response('404 Not Found', [])
            return []
    else:
        application = _application

    # Run the WSGI CGI handler with that application.
    util.run_wsgi_app(application)

if __name__ == '__main__':
    main()
