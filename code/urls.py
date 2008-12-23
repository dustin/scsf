from django.conf.urls.defaults import *
from scsf.apps.volunteers.models import Volunteer
from scsf.apps.grants.models import GrantRequest

urlpatterns = patterns('',
    # Example:
    # (r'^scsf/', include('scsf.apps.foo.urls.foo')),

    (r'^programs/', 'scsf.apps.general.views.programs'),

    # Special admin pages
    (r'^admin/grant/$',
        'scsf.apps.general.views.limited_object_list',
        {'queryset': GrantRequest.objects.all().order_by('-req_date')}),
    (r'^admin/grant/(?P<object_id>\d+)/$',
        'scsf.apps.general.views.limited_object_detail',
        {'queryset': GrantRequest.objects.all()}),

    (r'^admin/', include('django.contrib.admin.urls')),

    (r'^volunteer/new/', 'django.views.generic.create_update.create_object',
        {'post_save_redirect':'/volunteer/saved/',
            'model': Volunteer}),
    (r'^grant/new/', 'django.views.generic.create_update.create_object',
        {'post_save_redirect':'/grant/saved/',
            'model': GrantRequest}),
)
