from django.conf.urls.defaults import *

urlpatterns = patterns('',
    # Example:
    # (r'^scsf/', include('scsf.apps.foo.urls.foo')),
    (r'^grant/new/', 'scsf.apps.grants.views.form.new'),
    (r'^volunteer/new/', 'scsf.apps.volunteers.views.form.new'),

    # The donation form
    (r'^donate/', 'scsf.apps.donations.views.form.new'),
    # This is called when a donation is confirmed.
    (r'^donated/(?P<donationId>\d+)/',
        'scsf.apps.donations.views.form.confirm'),
    # This is called when a donation is cancelled.
    (r'^donateCancelled/(?P<donationId>\d+)/',
        'scsf.apps.donations.views.form.cancel'),

    (r'^programs/', 'scsf.apps.main.views.index.programs'),
    (r'^page/(?P<page>[A-z]+)', 'scsf.apps.main.views.index.page'),
)
