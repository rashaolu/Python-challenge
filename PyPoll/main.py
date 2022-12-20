# This is the code for PyPoll assignment 
import os
import csv 

csvpath= os.path.join('Resources','election_data.csv')

with open(csvpath ,encoding='utf-8-sig') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')

    csvheader=next(csvfile)
    print(f"header:{csvheader}")
    




