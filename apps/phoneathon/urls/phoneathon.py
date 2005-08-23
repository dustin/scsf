from django.conf.urls.defaults import *

info_dict = {
    'app_label': 'phoneathon',
    'module_name': 'phonevolunteers',
    'post_save_redirect': '/phoneathon/thanks/',
}

urlpatterns = patterns('',
    (r'^new/', 'django.views.generic.create_update.create_object',
        info_dict),
)
