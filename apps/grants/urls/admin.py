from django.conf.urls.defaults import *

info_dict = {
    'app_label': 'grants',
    'module_name': 'grantrequests',
}

urlpatterns = patterns('django.views.generic.list_detail',
    (r'^list/$', 'object_list', info_dict),
    (r'^show/(?P<object_id>\d+)/$', 'object_detail', info_dict),
)
