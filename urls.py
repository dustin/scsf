from django.conf.urls.defaults import *
from scsf.apps.volunteers.models import Volunteer
from scsf.apps.grants.models import GrantRequest

urlpatterns = patterns('',
    # Example:
    # (r'^scsf/', include('scsf.apps.foo.urls.foo')),

    (r'^donate/', 'scsf.apps.donations.views.newform'),
    # This is called when a donation is confirmed.
    (r'^donated/(?P<donationId>\d+)/', 'scsf.apps.donations.views.confirm'),

    # The donation form
    (r'^programs/', 'scsf.apps.general.views.programs'),

    # Uncomment this for admin:
    (r'^admin/', include('django.contrib.admin.urls')),

    (r'^volunteer/new/', 'django.views.generic.create_update.create_object',
        {'post_save_redirect':'/volunteer/saved/',
            'model': Volunteer}),
    (r'^grant/new/', 'django.views.generic.create_update.create_object',
        {'post_save_redirect':'/grant/saved/',
            'model': GrantRequest}),
)
