from django.core import template_loader
from django.shortcuts import render_to_response
from scsf.apps.scholarships.models import Scholarship

def programs(request):
    s = Scholarship.objects.order_by('-year')
    return render_to_response('programs.html', {'scholarships': s})

def page(request, page):
    t = template_loader.get_template(page)
    return render_to_response(page, {})

