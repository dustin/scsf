from django.conf.urls.defaults import *

urlpatterns = patterns('',
    # Example:
    # (r'^scsf/', include('scsf.apps.foo.urls.foo')),
    (r'^grant/new/', 'scsf.apps.grants.views.form.new'),
    (r'^volunteer/new/', 'scsf.apps.volunteers.views.form.new'),
    (r'^programs/', 'scsf.apps.main.views.index.programs'),
    (r'^page/(?P<page>[A-z]+)', 'scsf.apps.main.views.index.page'),
    (r'^$', 'scsf.apps.main.views.index.page', {'page': 'index'}),
)
