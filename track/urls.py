from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('track.views',
    url(r'^dashboard/$', 'stats', name='track-dashboard'),
)
