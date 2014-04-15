try:
    from django.conf.urls import patterns, include, url
except ImportError:
    # Django <= 1.4
    from django.conf.urls.defaults import patterns, include, url
from views import doc, howto

urlpatterns = patterns('',
    (r'^doc', doc),
    (r'^howto', howto),
)
