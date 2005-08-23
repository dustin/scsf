from django.conf.urls.defaults import *

urlpatterns = patterns('',
    # Example:
    # (r'^scsf/', include('scsf.apps.foo.urls.foo')),

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

    (r'^phoneathon/', include('scsf.apps.phoneathon.urls.phoneathon')),

    (r'^grant/', include('scsf.apps.grants.urls.grants')),
    (r'^volunteer/new/', 'scsf.apps.volunteers.views.form.new'),
)
