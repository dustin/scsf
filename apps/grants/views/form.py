#!/usr/bin/env python
"""

Copyright (c) 2005  Dustin Sallings <dustin@spy.net>
"""

from django.core import template_loader
from django.core.extensions import DjangoContext as Context
from django.models.grants import schools, grades, grantrequests
from django.utils.httpwrappers import HttpResponse

def show(request):
    school_list = schools.get_list(order_by=['name'])
    grade_list = grades.get_list(order_by=['id'])
    t = template_loader.get_template('grantform')
    c = Context(request, {
        'schools': school_list,
        'grades': grade_list,
    })
    return HttpResponse(t.render(c))

def new(request):
    t = template_loader.get_template('grantsaved')
    c = Context(request, {})
    return HttpResponse(t.render(c))
