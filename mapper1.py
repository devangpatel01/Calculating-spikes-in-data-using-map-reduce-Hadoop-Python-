#!/usr/bin/env python

from datetime import datetime
import sys
import time

for line in sys.stdin:
    line=line.strip()
    website,start,end=line.split('\t',2)
    date,time=start.split(" ")
    #print(date)
    start = datetime.strptime(start, '%Y-%m-%d %H:%M:%S')
    end = datetime.strptime(end, '%Y-%m-%d %H:%M:%S')
    diff=int(end.strftime("%s"))-int(start.strftime("%s"))
    comb=website+" "+date
    print('%s\t%s' % (comb,diff))
