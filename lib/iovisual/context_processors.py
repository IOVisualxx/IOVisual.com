from django.conf import settings
from django.utils.safestring import mark_safe

from .models import Verbiage


#//ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js


def load_verbiage():
    verbiage = settings.X_DEFAULT_VERBIAGE
    verbiage.update(Verbiage.fetch().to_json())
    return verbiage
    

def main_context(request, 
    setting_params=(
        'X_CANONICAL_URL',
        'X_SCRIPTS_MINIFIED',
        'X_SCRIPTS',
        'X_STYLES_MINIFIED',
        'X_SITE_NAME',
        'X_JQUERY_URL',
        'DEBUG',
        'MEDIA_URL',
    ), base='base.html'):
    context = {k: getattr(settings, k) for k in setting_params}
    context.update(VERBIAGE=load_verbiage(), BASE=base, request=request)
    return context
