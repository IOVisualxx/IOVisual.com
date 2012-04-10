from django.http import HttpResponseRedirect
from google.appengine.api import users


def login(request):
    return HttpResponseRedirect(users.create_login_url('/'))


def logout(request):
    return HttpResponseRedirect(users.create_logout_url('/'))
