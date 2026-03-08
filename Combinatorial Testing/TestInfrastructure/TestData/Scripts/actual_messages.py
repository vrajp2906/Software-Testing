import os
import json


expected_output = '../ExpectedOutput'
actual_output = '../ActualOutput'
actual_messages = '../ActualMessages'

def compare_json_files(expected_file, actual_file):
    with open(expected_file) as expected, open(actual_file) as actual:
        return json.load(expected) == json.load(actual)

def generate_actual_message(test_case_id):
    actual_file = f"{actual_output}/test{test_case_id}.json"
    expected_file = f"{expected_output}/test{test_case_id}.json"
    message_file = f"{actual_messages}/test{test_case_id}_message.txt"

    with open(message_file, 'w') as mf:
        if os.path.exists(actual_file) and os.path.exists(expected_file):
            mf.write(f"Test file {test_case_id} has matched. Everything is the same.\n"
                     if compare_json_files(expected_file, actual_file)
                     else f"Match Failed for test{test_case_id}.\n")
        else:
            mf.write(f"Test {test_case_id}: File is missing.\n")

for i in range(1, 17):
    generate_actual_message(i)

print("Check the ActualMessages folder for details.")

