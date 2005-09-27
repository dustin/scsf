#!/usr/bin/env python
"""

Copyright (c) 2005  Dustin Sallings <dustin@spy.net>
"""

import csv
import time

from django.models.donations import donations
from django.utils.httpwrappers import HttpResponse

def __writeCsv(f):
    cols=("ts", "name", "amt", "address1", "address2", "city", "zipcode",
        "email", "phone")

    l = donations.get_list(completed__exact=True)
    w=csv.writer(f)
    w.writerow(cols)
    w.writerows([[getattr(o, c) for c in cols] for o in l])

def getCsv(request):
    """Get a PDF of the given object."""
    pdfdata=None
    res=HttpResponse('', "text/csv")
    fn="scsf-donation-export-%s.csv" % (time.strftime("%Y%m%d"),)
    res["Content-Disposition"]="attachment; filename=%s" % (fn,)
    __writeCsv(res)
    return res

if __name__ == '__main__':
    import sys
    __writeCsv(sys.stdout)
