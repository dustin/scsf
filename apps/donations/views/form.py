#!/usr/bin/env python
"""

Copyright (c) 2005  Dustin Sallings <dustin@spy.net>
"""

import urllib

from django.core import template_loader, formfields
from django.core.extensions import DjangoContext as Context
from django.models.donations import donations
from django.utils.httpwrappers import HttpResponse, HttpResponseRedirect

def __getPayPalUrl(ob):
    # checkout="http://bleu.west.spy.net/cgi-bin/test.py"
    checkout="https://www.paypal.com/cgi-bin/webscr"
    baseurl='http://www.santaclaraschoolsfoundation.org/'
    args=[('cmd', '_xclick'),
        ('business', 'donations@santaclaraschoolsfoundation.org'),
        ('item_name', 'Donation'),
        ('no_shipping', '1'),
        ('return', baseurl + "donated/%d/" % ob.id),
        ('cancel_return', baseurl + 'donateCancelled/%d/' % ob.id),
        ('no_note', '1'),
        ('currency_code', 'USD'),
        ('tax', '0'),
        ('amount', '%.2f' % ob.amt),
        ]
    queryParam='&'.join([a + '=' + urllib.quote(b) for a, b in args])

    return HttpResponseRedirect(checkout + "?" + queryParam)

def new(request):
    """Entry point for new donations."""
    manipulator = donations.AddManipulator()

    if request.POST:
        new_data = request.POST.copy()
        # Need to specify the default value here. 1 == Null (*shrug*)
        new_data['completed']='1'
        errors = manipulator.get_validation_errors(new_data)

        if not errors:
            manipulator.do_html2python(new_data)
            new_place = manipulator.save(new_data)

            return __getPayPalUrl(new_place)
    else:
        errors = {}
        new_data = {'name': 'Anonymous'}

    form = formfields.FormWrapper(manipulator, new_data, errors)
    t = template_loader.get_template('donationform')
    c = Context(request, { 'form': form, 'errors': errors })
    return HttpResponse(t.render(c))

def confirm(request, donationId):
    """Invoked when we can confirm a donation was processed by paypal."""
    donation = donations.get_object(pk=donationId)
    donation.completed=True
    donation.save()
    t = template_loader.get_template('donationsaved')
    return HttpResponse(t.render(Context(request, {})))

def cancel(request, donationId):
    """Invoked when a user cancels from within paypal."""
    donation = donations.get_object(pk=donationId)
    donation.completed=False
    donation.save()
    t = template_loader.get_template('donationcancelled')
    return HttpResponse(t.render(Context(request, {})))
