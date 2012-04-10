from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template

from news.models import NewsItem

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', direct_to_template, {'template': 'index.html', 'extra_context': {
      'videography': 'videography/top.html',
      'news': 'toptopic/top_news.html',
      'top_news': NewsItem.list_recent,
    }}, name='index'),
    url(r'^about$', direct_to_template, {'template': 'about.html'}, name='about'),
    url(r'^contact$', direct_to_template, {'template': 'contact.html'}, name='contact'),
)
#) + patterns('',
    #url(r'^login$', 'iovisual.utils.views.login', name='login'),
    #url(r'^logout$', 'iovisual.utils.views.logout', name='logout'),

    # Examples:
    # url(r'^$', 'iovisual.views.home', name='home'),
    # url(r'^iovisual/', include('iovisual.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
#)
