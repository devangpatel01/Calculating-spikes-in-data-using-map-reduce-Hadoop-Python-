#!/usr/bin/env python


import sys

prevwebsite=None
sumspike=0
for line in sys.stdin:
    line=line.strip()
    website,spike=line.split('\t',1)
    spike=int(spike)
    if website == prevwebsite:
       sumspike=sumspike+spike
    else:
       if sumspike > 0:
          print('%s\t%s' % (prevwebsite,sumspike))
       sumspike=0
       sumspike=sumspike+spike
       prevwebsite=website
print('%s\t%s' % (prevwebsite,sumspike))
