import csv
import dbf
import os
import sys

filename = "/Users/alenalapteva/Documents/Banks bot/Нормативы ЦБ/135-20160201/012016_135_5.dbf"
if filename.endswith('.dbf'):
    csv_fn = filename[:-4]+ ".csv"
    with open(csv_fn,'wb') as csvfile:
        in_db = dbf.Table(filename)
        in_db.export(filename=csv_fn, header=False)
else:
    print ("Filename does not end with .dbf")