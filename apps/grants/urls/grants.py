from django.conf.urls.defaults import *

info_dict = {
    'app_label': 'grants',
    'module_name': 'grantrequests',
    'post_save_redirect': '/grant/saved/'
}

urlpatterns = patterns('',
    (r'^new/', 'django.views.generic.create_update.create_object',
        info_dict),
)
