from django.conf.urls.defaults import *

urlpatterns = patterns('',
    # Admin stuff
    (r'^grant/', include('scsf.apps.grants.urls.admin')),
    (r'^donation/', include('scsf.apps.donations.urls.admin')),
    (r'^phoneathon/', include('scsf.apps.phoneathon.urls.admin')),
    (r'^admin/', include('django.contrib.admin.urls.admin')),
)
