#!/usr/bin/env python
"""

Copyright (c) 2005  Dustin Sallings <dustin@spy.net>
"""

from django.core import template_loader, formfields
from django.core.extensions import DjangoContext as Context
from django.models.grants import schools, grades, grantrequests
from django.utils.httpwrappers import HttpResponse

def show(request):
    form = formfields.FormWrapper(grantrequests.AddManipulator(), {}, {})
    t = template_loader.get_template('grantform')
    c = Context(request, { 'form': form })
    return HttpResponse(t.render(c))

def new(request):
    t = template_loader.get_template('grantsaved')
    c = Context(request, {})
    return HttpResponse(t.render(c))
