#!/usr/bin/env python
"""

Copyright (c) 2005  Dustin Sallings <dustin@spy.net>
"""

import csv
import time

from django.models.donations import donations, prioritys
from django.utils.httpwrappers import HttpResponse

def __writeCsv(f):
    dcols=["ts", "name", "amt", "address1", "address2", "city", "zipcode",
        "email", "phone"]

    # Get the list of priorities and their names in alphabetical order
    pnames = [o.name for o in prioritys.get_list()]
    pnames.sort()

    l = donations.get_list(completed__exact=True)

    rows=[]
    for d in l:
        r=[getattr(d, c) for c in dcols]
        myPNames = [o.name for o in d.get_priority_list()]
        r.extend([(x in myPNames) for x in pnames])
        rows.append(r)

    w=csv.writer(f)
    w.writerow(dcols + pnames)
    w.writerows(rows)

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
