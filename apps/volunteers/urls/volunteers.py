from django.conf.urls.defaults import *

info_dict = {
    'app_label': 'volunteers',
    'module_name': 'volunteers',
    'post_save_redirect': '/volunteer/saved/'
}

urlpatterns = patterns('',
    (r'^new/', 'django.views.generic.create_update.create_object',
        info_dict)
)
