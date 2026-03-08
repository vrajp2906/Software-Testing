# References:
# https://www.w3schools.com/python/python_json.asp
# https://docs.python.org/3/library/csv.html
# https://docs.python.org/3/library/os.html
# https://www.datacamp.com/tutorial/python-subprocess

import os
import csv
import json

test_files = "../TestFiles"
expected_output = "../ExpectedOutput"

def csv_to_json(input_file, output_file):
    with open(input_file, mode='r') as csv_file:
        reader = csv.DictReader(csv_file)
        data = [row for row in reader]
        with open(output_file, mode='w') as json_file:
            json.dump(data, json_file, indent=4, ensure_ascii=False)
            
for csv_f in os.listdir(test_files):
    if csv_f.endswith(".csv"):
        csv_file_path = os.path.join(test_files, csv_f)
        json_file_name = csv_f.replace('.csv', '.json')
        json_file_path = os.path.join(expected_output, json_file_name)

        csv_to_json(csv_file_path, json_file_path)
        print(f"Generated expected output: {json_file_path}")


