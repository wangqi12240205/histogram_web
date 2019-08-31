import csv
import json
import os
 

data_path = 'data'
output_path = 'json'
file_list = [os.path.join(data_path, f) for f in os.listdir(data_path) if f.endswith('.csv')]
for csv_file in file_list:
    f = open(csv_file)
    reader = csv.DictReader(f)
    out = json.dumps( [ row for row in reader ] )  
    pre, ext = os.path.splitext(csv_file)
    f_json = open(os.path.join(output_path, os.path.basename(pre) + '.json'), 'w')  
    f_json.write(out)  

