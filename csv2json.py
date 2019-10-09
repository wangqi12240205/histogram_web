import csv
import json
import os
import pandas as pd

 # transfter data inyo json
raw_path = 'raw'
data_path = 'data'
output_path = 'json'
raw_files = [os.path.join(raw_path, f) for f in os.listdir(raw_path) if f.endswith('.csv')]

for csv_file in raw_files:
    if csv_file.endswith('list_measure.csv'):
        pd.read_csv(csv_file, header=None, dtype=str).to_csv(os.path.join(data_path, os.path.basename(csv_file)), header=False, index=False)
        continue
    pd.read_csv(csv_file, header=None, dtype=str).T.to_csv(os.path.join(data_path, os.path.basename(csv_file)), header=False, index=False)

data_files = [os.path.join(data_path, f) for f in os.listdir(data_path) if f.endswith('.csv')]

for csv_file in data_files:
    f = open(csv_file)
    reader = csv.DictReader(f)
    out = json.dumps( [ row for row in reader ] )  
    pre, ext = os.path.splitext(csv_file)
    out = os.path.basename(pre) + " = " + out 
    f_json = open(os.path.join(output_path, os.path.basename(pre) + '.json'), 'w')  
    f_json.write(out)  

