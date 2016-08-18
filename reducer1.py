#!/usr/bin/env python

 

import sys

prevkey=None
duration=0
ctr=0
avg=0.0
for line in sys.stdin:
    key,time=line.split("\t",1)
    time=int(time)
    if key == prevkey:
       duration=duration+time
       ctr=ctr+1
    else:
       if ctr > 0:
          avg=duration/ctr
          avg=int(avg)
          print('%s\t%s' % (prevkey,avg))
       duration=0
       avg=0
       ctr=0
       duration=duration+time
       ctr=ctr+1
    prevkey=key
print('%s\t%s' % (prevkey,duration))

