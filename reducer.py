#!/usr/bin/env python

import sys

prevkey=None
currentsales=0.0
for line in sys.stdin:
    line=line.strip()
    key,sales=line.split('\t',1)
    sales=float(sales)
    if key == prevkey:
       currentsales=currentsales+sales
    else:
       if currentsales > 25000000.0:
          print('%s\t%s' % (prevkey,currentsales))
       currentsales=0.0
       currentsales=currentsales+sales
       prevkey=key
if currentsales > 25000000.0:
   print('%s\t%s' % (prevkey,currentsales))
