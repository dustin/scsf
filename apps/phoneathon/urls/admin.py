from django.conf.urls.defaults import *

info_dict = {
    'app_label': 'phoneathon',
    'module_name': 'phonevolunteers',
}

urlpatterns = patterns('',
    (r'^list/$', 'django.views.generic.list_detail.object_list', info_dict),
    (r'^csv/$', 'scsf.apps.phoneathon.views.csvexport.getCsv'),
    (r'^show/(?P<object_id>\d+)/$',
        'django.views.generic.list_detail.object_detail', info_dict),
)
