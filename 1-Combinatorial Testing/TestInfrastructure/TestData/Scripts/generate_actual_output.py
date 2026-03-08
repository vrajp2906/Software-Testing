import os
import subprocess

test_files = "../TestFiles"
actual_output = "../ActualOutput"

def using_tool(input_file, output_file):
    with open(output_file, mode='w') as json_file:
        subprocess.run(['csvtojson', input_file], stdout=json_file)

for csv_file_name in os.listdir(test_files):
    if csv_file_name.endswith(".csv"):
        csv_file_path = os.path.join(test_files, csv_file_name)
        json_file_name = csv_file_name.replace('.csv', '.json')
        json_file_path = os.path.join(actual_output, json_file_name)
        
        using_tool(csv_file_path, json_file_path)
        print(f"Generated actual output: {json_file_path}")


