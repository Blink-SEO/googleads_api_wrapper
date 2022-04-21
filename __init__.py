import os
import csv

with open(os.path.dirname(__file__) + r'/google_ads_location_ids.csv', mode='r') as infile:
    reader = csv.reader(infile)
    LOCATION_ID_DICT = {rows[1]: rows[2] for rows in reader}

