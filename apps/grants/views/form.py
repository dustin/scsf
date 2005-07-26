#!/usr/bin/env python
"""

Copyright (c) 2005  Dustin Sallings <dustin@spy.net>
"""

from django.core import template_loader, formfields
from django.core.extensions import DjangoContext as Context
from django.models.grants import grantrequests
from django.utils.httpwrappers import HttpResponse

def new(request):
    manipulator = grantrequests.AddManipulator()

    if request.POST:
        new_data = request.POST.copy()
        # Need to specify the default value here. 1 == Null (*shrug*)
        new_data['accepted']='1'
        errors = manipulator.get_validation_errors(new_data)

        if not errors:
            manipulator.do_html2python(new_data)
            new_place = manipulator.save(new_data)

            t = template_loader.get_template('grantsaved')
            c = Context(request, {})
            return HttpResponse(t.render(c))
    else:
        errors = new_data = {}

    form = formfields.FormWrapper(manipulator, new_data, errors)
    t = template_loader.get_template('grantform')
    c = Context(request, { 'form': form, 'errors': errors })
    return HttpResponse(t.render(c))
