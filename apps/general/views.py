from django.core import template_loader
from django.shortcuts import render_to_response
from django.views.generic.list_detail import object_detail, object_list
from django.contrib.auth.decorators import login_required
from scsf.apps.scholarships.models import Scholarship

def programs(request):
    s = Scholarship.objects.order_by('-year')
    return render_to_response('programs.html', {'scholarships': s})

def page(request, page):
    t = template_loader.get_template(page)
    return render_to_response(page, {})

@login_required
def limited_object_detail(*args, **kwargs):
    return object_detail(*args, **kwargs)

@login_required
def limited_object_list(*args, **kwargs):
    return object_list(*args, **kwargs)
