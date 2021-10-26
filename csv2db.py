import csv
from database.operations import insert
import os
from pprint import pprint as pp
from termcolor import cprint
from tqdm import tqdm
os.system('color')

cprint(f"\n Processing CSV file...", "green", attrs=['reverse'])

num_lines = sum(1 for line in open('data.csv', encoding="'utf-8"))

with tqdm (total=num_lines) as pbar:

    with open('data.csv', newline='') as f:
        reader = csv.reader(f, delimiter=';')

        line_count = 0

        for row in reader:
            if line_count!=0:
                result = insert(name=row[0], address=row[1], postcode=row[2], city=row[3], 
                                date=row[5], type=row[6], business_id=row[7])
                #print(f"Inserted row number {line_count} with id={result}")
                
            line_count+=1
            pbar.update(1)
pbar.close()