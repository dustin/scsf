from django.conf.urls.defaults import *

info_dict = {
    'app_label': 'donations',
    'module_name': 'donations',
}

urlpatterns = patterns('',
    (r'^list/$', 'django.views.generic.list_detail.object_list',
        dict(info_dict, extra_lookup_kwargs={'completed__exact': True})),
    (r'^csv/$', 'scsf.apps.donations.views.csvexport.getCsv'),
    (r'^show/(?P<object_id>\d+)/$',
        'django.views.generic.list_detail.object_detail', info_dict),
    (r'^pdf/(?P<object_id>\d+)/$',
        'scsf.apps.donations.views.pdfthanks.getPdf'),
)
