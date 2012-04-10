import os, sys

sys.path[:0] = [
    os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'lib'))]


# Must set this env var before importing any part of Django
# 'project' is the name of the project created with django-admin.py
os.environ['DJANGO_SETTINGS_MODULE'] = 'iovisual.settings_dev'

# Force Django to reload its settings.
#from django.conf import settings
#settings._target = None

#import logging
import django.core.handlers.wsgi
#import django.core.signals

#def log_exception(*args, **kwds):
#    logging.exception('Exception in request:')

# Log errors.
#django.core.signals.got_request_exception.connect(log_exception)

application = django.core.handlers.wsgi.WSGIHandler()
