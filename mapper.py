#!/usr/bin/env python

import sys

for line in sys.stdin:
    line=line.strip()
    store,dept,date,sales=line.split('\t',3)
    year=int(date.split('-',1)[0])
    dept=int(dept)
    key=str(dept)+" "+str(year)
    print('%s\t%s' % (key,sales))
