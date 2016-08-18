#!/usr/bin/env python

import sys
import os
import csv
import datetime
from datetime import date,timedelta

for line in sys.stdin:
    line=line.strip()
    websitedate,avgtime=line.split('\t',1)
    print('%s\t%s' % (websitedate,avgtime))
    
