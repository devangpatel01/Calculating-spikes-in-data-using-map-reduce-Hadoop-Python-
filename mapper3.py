#!/usr/bin/env python

import sys


for line in sys.stdin:
    line=line.strip()
    website,spike=line.split('\t',1)
    print('%s\t%s' % (website,spike))
    
