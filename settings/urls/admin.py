from django.conf.urls.defaults import *

urlpatterns = patterns('',
    # (r'^admin/', include('django.conf.urls.admin')),
    (r'^grant/', include('scsf.apps.grants.urls.admin')),
    (r'^admin/', include('django.conf.urls.admin')),
)
