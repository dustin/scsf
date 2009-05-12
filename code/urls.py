from django.conf.urls.defaults import *
from scsf.apps.volunteers.models import Volunteer
from scsf.apps.grants.models import GrantRequest

urlpatterns = patterns('',
    # Example:
    # (r'^scsf/', include('scsf.apps.foo.urls.foo')),

    # Special admin pages
    (r'^admin/grant/(?P<object_id>\d+)/$',
        'scsf.apps.general.views.limited_object_detail',
        {'queryset': GrantRequest.objects.all()}),

    (r'^admin/', include('django.contrib.admin.urls')),

)
