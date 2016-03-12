import csv
from dbfpy import dbf
import os
import sys

filename = "/Users/alenalapteva/Documents/Banks bot/Нормативы ЦБ/135-20160201/012016_135_5.dbf"
if filename.endswith('.dbf'):
    csv_fn = filename[:-4]+ ".csv"
    with open(csv_fn,'wb') as csvfile:
        in_db = dbf.Dbf(filename)
        out_csv = csv.writer(csvfile)
        names = []
        for field in in_db.header.fields:
            names.append(field.name)
        out_csv.writerow(names)
        for rec in in_db:
            out_csv.writerow(rec.fieldData)
        in_db.close()

else:
  print ("Filename does not end with .dbf")