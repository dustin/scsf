#!/usr/bin/env python
"""

Copyright (c) 2005  Dustin Sallings <dustin@spy.net>
"""

from django.core import template_loader, formfields
from django.core.extensions import DjangoContext as Context
from django.models.volunteers import volunteers
from django.utils.httpwrappers import HttpResponse

def new(request):
    manipulator = volunteers.AddManipulator()

    if request.POST:
        new_data = request.POST.copy()
        errors = manipulator.get_validation_errors(new_data)

        if not errors:
            manipulator.do_html2python(new_data)
            new_place = manipulator.save(new_data)

            t = template_loader.get_template('volunteersaved')
            c = Context(request, {})
            return HttpResponse(t.render(c))
    else:
        errors = new_data = {}

    form = formfields.FormWrapper(manipulator, new_data, errors)
    t = template_loader.get_template('volunteerform')
    c = Context(request, { 'form': form, 'errors': errors })
    return HttpResponse(t.render(c))
