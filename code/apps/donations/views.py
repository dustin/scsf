import urllib

from django.forms import FormWrapper
from django.template import RequestContext as Context
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect

from scsf.apps.donations.models import Donation
    
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

def newform(request):
    """Entry point for new donations."""
    manipulator = Donation.AddManipulator()

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

    form = FormWrapper(manipulator, new_data, errors)
    return render_to_response('donationform.html',
        {'form': form, 'errors': errors})

def confirm(request, donationId):
    """Invoked when we can confirm a donation was processed by paypal."""
    donation = Donation.get(id=donationId)
    donation.completed=True
    donation.save()
    return render_to_response('donationsaved.html', {})

def cancel(request, donationId):
    """Invoked when a user cancels from within paypal."""
    donation = Donation.get(id=donationId)
    donation.completed=False
    donation.save()
    return render_to_response('donationcancelled.html', {})
