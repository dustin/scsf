#!/usr/bin/env python
"""

Copyright (c) 2005  Dustin Sallings <dustin@spy.net>
"""

import csv
import time

from django.models.phoneathon import whentohelps, phonevolunteers
from django.utils.httpwrappers import HttpResponse

def __writeCsv(f):
    dcols=["timestamp", "name", "address", "city", "zipcode",
        "email", "phone",]

    # Get the list of priorities and their names in alphabetical order
    wnames = [o.name for o in whentohelps.get_list()]

    l = phonevolunteers.get_list()

    rows=[]
    for d in l:
        r=[getattr(d, c) for c in dcols]
        r.append(d.get_school())
        myWNames = [o.name for o in d.get_whentohelp_list()]
        r.extend([(x in myWNames) for x in wnames])
        rows.append(r)

    w=csv.writer(f)
    w.writerow(dcols + ["school"] + wnames)
    w.writerows(rows)

def getCsv(request):
    """Get a CSV export of all of the phone volunteers."""
    res=HttpResponse('', "text/csv")
    fn="scsf-phoneathon-export-%s.csv" % (time.strftime("%Y%m%d"),)
    res["Content-Disposition"]="attachment; filename=%s" % (fn,)
    __writeCsv(res)
    return res

if __name__ == '__main__':
    import sys
    __writeCsv(sys.stdout)
