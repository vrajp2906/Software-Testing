import os
import difflib

expected_dir = '../ExpectedOutput'
actual_dir = '../ActualOutput'
actual_messages = '../ActualMessages'
comparison_log_file = os.path.join(actual_messages, 'comparison_log.txt')

def file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

def write_diff_to_log(diff, file_name, log_file):
    log_file.write(f"\n{'='*50}\n")
    log_file.write(f"Differences for {file_name}:\n")
    log_file.write(f"{'='*50}\n\n")
    for line in diff:
        log_file.write(line)

with open(comparison_log_file, 'w') as log_file:
    log_file.write("Comparison Log:\n")
    log_file.write("="*50 + "\n\n")

    for expected_file in os.listdir(expected_dir):
        expected_file_path = os.path.join(expected_dir, expected_file)
        actual_file_path = os.path.join(actual_dir, expected_file)

        if os.path.exists(actual_file_path):
            expected_content = file(expected_file_path)
            actual_content = file(actual_file_path)

            diff = list(difflib.unified_diff(expected_content, actual_content,
                                             fromfile='Expected Output',
                                             tofile='Actual Output'))

            if diff:
                write_diff_to_log(diff, expected_file, log_file)
            else:
                log_file.write(f"No differences for {expected_file}\n")



