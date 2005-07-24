from django.conf.urls.defaults import *

urlpatterns = patterns('',
    # Example:
    # (r'^scsf/', include('scsf.apps.foo.urls.foo')),
    (r'^page/(?P<page>[A-z]+)', 'scsf.apps.main.views.index.page'),
    (r'^$', 'scsf.apps.main.views.index.page', {'page': 'index'}),
)
