from django.conf.urls.defaults import *

urlpatterns = patterns('',
    # Example:
    # (r'^scsf/', include('scsf.apps.foo.urls.foo')),
    (r'', 'scsf.apps.main.views.index.index'),
)
