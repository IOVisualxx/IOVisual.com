import functools
import urlparse

from django.http import HttpResponseRedirect
from django.http.QueryDict import QueryDict


def friendy_fragment(view):
    """Let hash fragment be understood by crawlers. 

    Based on Facebook and Twitter."""

    @functools.wraps(view)
    def wrapper(request, *args, **kwargs):
        # TODO: fragments will be to long

        fragment = request.GET.get('_escaped_fragment_')
        if not fragment:
            return
        p = urlparse.urlparse(hash_)
        path = p.path
        get = QueryDict(p.query)
        
        uri = get.get('uri')
        if not uri:

        if get.get('redirect'):
            return HttpResponseRedirect(_hash_to_url(hash_))


