from django.conf.urls.defaults import *

urlpatterns = patterns('',
    # Example:
    # (r'^scsf/', include('scsf.apps.foo.urls.foo')),
    (r'^programs', 'scsf.apps.main.views.index.programs'),
    (r'^funding', 'scsf.apps.main.views.index.funding'),
    (r'', 'scsf.apps.main.views.index.index'),
)
