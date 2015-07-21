#!/usr/bin/python

import csv
from dbfpy import dbf
import os
import sys

filename = sys.argv[1]
if filename.endswith('.dbf'):
    print "Converting %s to csv" % filename
    out_csv = filename[:-4]+ ".csv"
    in_db = dbf.Dbf(filename)
    names = []
    cn0 = in_db.header.fields[3].name
    cn2 = in_db.header.fields[18].name
    names.append(cn0)
    names.append(cn2)
    wb = open(out_csv,'a')
    wb.write(str(names))
    wb.write('\n')
    for rec in range(0,len(in_db)):
     v1 = in_db[rec].fieldData[3]
     v2 = in_db[rec].fieldData[18]
     data2 = str(v1)+','+str(v2)
     wb.write(data2)
     wb.write('\n')
    wb.close()
    in_db.close()
    print "Done..."
# awk -F ',' '{print $4,$19}' wdpaid_Aby_Mount_areas.csv > wdpaid_Aby_Mount_areas2.csv
else:
  print "Filename does not end with .dbf"
