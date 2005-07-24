#!/usr/bin/env python
"""

Copyright (c) 2005  Dustin Sallings <dustin@spy.net>
"""
# arch-tag: 4970296-44-119-8187-0030187026

from django.core import template_loader
from django.core.extensions import DjangoContext as Context
from django.models.grants import schools
from django.utils.httpwrappers import HttpResponse

def index(request):
    school_list = schools.get_list(order_by=['name'])
    t = template_loader.get_template('index')
    c = Context(request, {
        'schools': school_list,
    })
    return HttpResponse(t.render(c))

def programs(request):
    t = template_loader.get_template('programs')
    c = Context(request, { })
    return HttpResponse(t.render(c))

def funding(request):
    t = template_loader.get_template('funding')
    c = Context(request, { })
    return HttpResponse(t.render(c))
