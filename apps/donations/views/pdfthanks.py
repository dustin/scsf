#!/usr/bin/env python
"""

Copyright (c) 2005  Dustin Sallings <dustin@spy.net>
"""
# arch-tag: 73793D7A-55B9-40F8-9C27-9C5B5510F19F

import re
import os
import time

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import ParagraphStyle
from reportlab.rl_config import defaultPageSize
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import inch

from django.core import template_loader, formfields
from django.core.extensions import DjangoContext as Context
from django.models.donations import donations
from django.utils.httpwrappers import HttpResponse, HttpResponseRedirect

DATEFMT="%B %d, %Y"
IMG_PATH="/data/web/purple-virts/admin.scsf.org/"

def comma_me(amount):
    orig = str(amount)
    new = re.sub("^(-?\d+)(\d{3})", '\g<1>,\g<2>', str(amount))
    if orig == new:
        return new
    else:
        return comma_me(new)

def getStyles():
    return {
        'main': ParagraphStyle('main', spaceAfter=0.25 * inch, fontSize=14,
        leading=16),
        'plain': ParagraphStyle('main', fontSize=14, leading=16),
        'footer': ParagraphStyle('Footer', fontSize=8, leading=10,
        alignment=TA_CENTER)}

def hasThing(x):
    return x is not None and x != ''

def go(filepath, parts):
    global IMG_PATH
    doc=SimpleDocTemplate(filepath, leftMargin=1.5*inch, topMargin=1.75*inch)

    styles=getStyles()

    stuff=[]
    stuff.append(Paragraph(parts['date'], styles['plain']))
    stuff.append(Spacer(1, 0.25*inch))
    stuff.append(Paragraph(parts['name'], styles['plain']))

    if hasThing(parts['address']):
        stuff.append(Paragraph(parts['address'], styles['plain']))
    if hasThing(parts['city']) and hasThing(parts['state']) \
        and hasThing(parts['zip']):
        stuff.append(Paragraph("%(city)s, %(state)s  %(zip)s" % parts,
            styles['plain']))

    # Post address
    stuff.append(Spacer(1, 0.25*inch))

    stuff.append(Paragraph("Dear %(name)s:" % parts, styles['main']))

    # Begin normal content

    stuff.append(Paragraph("""
Thank you for your recent donation of $%(amount)s to the Santa Clara Schools
Foundation. Your generous contribution is an investment in the future of our
community's children and ultimately everyone's future.
""" % parts, styles['main']))

    stuff.append(Paragraph("""
Since 1992 the foundation has been providing grants to individual classroom
teachers to help them enrich the learning experiences of their students and
that grant program will continue as before. The annual campaign to which you
have so generously responded will expand the foundation's efforts beyond
individual classrooms and enable us to help students on a district-wide basis.
As you obviously are aware, this is a critical need in these times of crippling
cuts to education funding.
""" % parts, styles['main']))

    stuff.append(Paragraph("""
Thank you again for your gift to the Santa Clara Schools Foundation. Your
contribution is genuinely appreciated and will be put to good use in improving
the education of our young people.
""" % parts, styles['main']))

    stuff.append(Paragraph("Sincerely,", styles['plain']))
    # Space before sig
    stuff.append(Spacer(1, 0.125*inch))

    # Signature here
    img=Image(os.path.join(IMG_PATH, "paulfrench.jpg"),
        width=2.5 * inch, height=0.40742 * inch)
    img.hAlign = 'LEFT'
    stuff.append(img)

    # space after sig
    # stuff.append(Spacer(1, 0.125*inch))

    stuff.append(Paragraph("Paul A. French", styles['plain']))
    stuff.append(Paragraph("President, Santa Clara Schools Foundation",
        styles['plain']))

    stuff.append(Spacer(1, 0.5*inch))

    stuff.append(Paragraph("""
Your contribution is fully tax deductible. No goods or services were provided
by the Santa Clara Schools Foundation in consideration for this contribution.
""" % parts, styles['footer']))

    doc.build(stuff)

def getPdf(request, object_id):
    """Get a PDF of the given object."""
    donation = donations.get_object(pk=object_id)
    fn="/tmp/scsf.thanks.%d.pdf" % int(object_id)
    pdfdata=None
    res=HttpResponse('', "application/pdf")
    go(res, {'name':donation.name,
        'date': time.strftime(DATEFMT),
        'address': donation.address1,
        'city': donation.city, 'state': 'CA', 'zip': donation.zipcode,
        'amount': comma_me("%.2f" % donation.amt)})
    return res

if __name__ == '__main__':
    go('/tmp/test.pdf', { 'name': "Dustin Sallings",
        'date':time.strftime(DATEFMT),
        'address': '2589 Borax Dr.',
        'city': 'Santa Clara', 'state': 'CA', 'zip': '95051',
        'amount': comma_me(8528522523.25)})
