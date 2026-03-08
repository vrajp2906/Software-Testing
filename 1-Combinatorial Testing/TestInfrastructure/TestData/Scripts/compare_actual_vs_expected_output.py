import os
import json
import re

expected_output = "../ExpectedOutput"
actual_output = "../ActualOutput"

def compare_json_files(expected_file, actual_file):
    with open(expected_file, mode='r') as expected, open(actual_file, mode='r') as actual:
        expected_data = json.load(expected)
        actual_data = json.load(actual)
        return expected_data == actual_data

def test_case(file_name):
    match = re.search(r'\d+', file_name)
    return int(match.group()) if match else float('inf')

json_files = [f for f in os.listdir(expected_output) if f.endswith(".json")]
json_files.sort(key=test_case)

for json_file_name in json_files:
    expected_file_path = os.path.join(expected_output, json_file_name)
    actual_file_path = os.path.join(actual_output, json_file_name)

    if os.path.exists(actual_file_path):
        if compare_json_files(expected_file_path, actual_file_path):
            print(f"{json_file_name}: PASSED")
        else:
            print(f"{json_file_name}: FAILED")
    else:
        print(f"{json_file_name}: Missing")


