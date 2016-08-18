#!/usr/bin/env python

import sys
import os
import datetime
from datetime import date,timedelta

avg1=0
avg2=0
ctr=0
ctr1=0
for line in sys.stdin:
    ctr1=ctr1+1
    line=line.strip()
    websitedate,avgtime=line.split('\t',1)
    website,date=websitedate.split(' ',1)
    #print('%s\t%s\t%s' % (website,date,avgtime))
    date=datetime.datetime.strptime(date, "%Y-%m-%d")
    if ctr == 0 :
       prevdate=date
       prevwebsite=None
       avg1=int(avgtime)
       avg2=int(avgtime)
    else:
       avg1=2 * avg2
       avg2=int(avgtime)
    currentdate=prevdate+timedelta(1)
    if website == prevwebsite:
       if date == currentdate:
          if avg2 >= avg1:
             if ctr1==3:
                print('%s\t%s' % (website,1))
                ctr1=0
          else:
             ctr1=0         
    prevwebsite=website
    prevdate=date
    ctr=1
