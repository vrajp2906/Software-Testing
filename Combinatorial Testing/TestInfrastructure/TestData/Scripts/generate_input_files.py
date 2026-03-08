import os
import csv

output_dir = "../TestFiles"

data = [
    ['name', 'age', 'city', 'job', 'pay', 'field', 'date', 'email', 'phone', 'country',
     'postal_code', 'address', 'degree', 'birth_date', 'emergency_contact', 'married', 'children',
     'gender'],
    ['Vraj Patel', 24, 'Vancouver', 'Software Engineer', 29062, 'IT', '2024-06-15', 'vrajp@gmail.com',
     '416-555-1234', 'Canada', 'V5E 4P1', '7000 21st ave', 'B.Sc.', '2028-03-26', 'N/A', 'Single', 0, 'M'],
    ['Dhruv Patel', '', 'Vancouver', 'Data Analyst', 75450, 'Analytics', '2025-10-01', '', '604-233-5678', 'Canada',
     'V5B 3R9', 'King george', 'B.Sci.', '2028-08-05', 'Neha Patel', 'Single', 0, 'F'],
    ['Rio P', 5, 'Calgary', 'Project Manager', '', 'Project Management', '2012-03-11', 'rio@hotmail.com',
     '455-555-9556', 'Canada', 'V2P 5G1', 'Burnaby Lougheed', 'MBA', '2000-09-18', 'Kriti S', 'Married', 5, 'F'],
    ['Mr Singh', 28, '', 'Mechanical Engineer', 85440, 'Civil', '2020-05-20', 'singh@live.com',
     '114-222-4321', 'Canada', 'K2Z 1Y7', 'Toronto St Downtown', 'B.Tech.', '1993-12-05', 'Mrs Singh', 'Single', 0, 'M'],
    ['Smit Patel', 29, 'Ottawa', 'Dentist', 90999, 'Doctor', '2016-08-30', 'smitp@gmail.com.com',
     '', 'Canada', 'V1A 0B1', 'Marine Drive', 'BBA', '1988-05-10', 'Unknown', 'Single', 1, 'F']
]

delimiter_map = {
    "Comma": ",",
    "Tab": "\t",
    "Semicolon": ";",
    "Pipe": "|",
    "Auto": ","  # Default for Auto
}

quote_map = {
    "DoubleQuote": '"',
    "SingleQuote": "'",
    "Off": ''
}

def for_trim(row):
    return [field.strip() if isinstance(field, str) else field for field in row]

def for_ignore_empty(row):
    return [None if field == '' else field for field in row]

def include_columns(row, headers, columns):
    included_indices = [i for i, header in enumerate(headers) if header in columns]
    return [row[i] for i in included_indices]

def exclude_columns(row, headers, columns):
    excluded_indices = [i for i, header in enumerate(headers) if header not in columns]
    max_index = len(row) - 1
    return [row[i] for i in excluded_indices if i <= max_index]

def for_csv(file_name, headers, rows, delimiter, quoting, quotechar, escapechar):
    file_path = os.path.join(output_dir, file_name)
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=delimiter, quoting=quoting, quotechar=quotechar, escapechar=escapechar)
        if headers:
            writer.writerow(headers)
        for row in rows:
            if quoting == csv.QUOTE_NONE:
                row = ['""' if field == '' or field is None else field for field in row]
            writer.writerow(row)
    print(f"CSV file generated: {file_name}")


def apply_max_row_length(rows, max_row_length):
    if max_row_length > 0:
        return [row[:max_row_length] for row in rows]
    return rows

def test_case_1():
    file_name = "test1.csv"
    headers_data = None  # No header for JSON output
    rows_data = [include_columns(row, data[0], ["name", "age"]) for row in data[1:]]
    rows_data = apply_max_row_length(rows_data, 65535)
    for_csv(file_name, headers_data, rows_data, delimiter_map["Comma"], csv.QUOTE_ALL, quote_map["SingleQuote"], '\\')

def test_case_2():
    file_name = "test2.csv"
    headers_data = None
    rows_data = [include_columns(row, data[0], ["city", "country", "postal_code"]) for row in data[1:]]
    rows_data = apply_max_row_length(rows_data, 0)  # No row length limit
    for_csv(file_name, headers_data, rows_data, delimiter_map["Comma"], csv.QUOTE_NONE, '', '\\')

def test_case_3():
    file_name = "test3.csv"
    headers_data = data[0]
    rows_data = data[1:]
    for_csv(file_name, headers_data, rows_data, delimiter_map["Comma"], csv.QUOTE_ALL, quote_map["DoubleQuote"], '\\')

def test_case_4():
    file_name = "test4.csv"
    headers_data = None  # JSON output
    rows_data = [exclude_columns(row, data[0], ["name"]) for row in data[1:]]
    for_csv(file_name, headers_data, rows_data, delimiter_map["Tab"], csv.QUOTE_NONE, '', '\\')

def test_case_5():
    file_name = "test5.csv"
    headers_data = None  # No header
    rows_data = [include_columns(row, data[0], ["name", "age"]) for row in data[1:]]
    for_csv(file_name, headers_data, rows_data, delimiter_map["Tab"], csv.QUOTE_ALL, quote_map["DoubleQuote"], '\\')

def test_case_6():
    file_name = "test6.csv"
    headers_data = data[0]
    rows_data = [include_columns(row, headers_data, ["city", "postal_code"]) for row in data[1:]]
    rows_data = apply_max_row_length(rows_data, 65535)
    for_csv(file_name, headers_data, rows_data, delimiter_map["Tab"], csv.QUOTE_ALL, quote_map["SingleQuote"], '')

def test_case_7():
    file_name = "test7.csv"
    headers_data = data[0]
    rows_data = [exclude_columns(row, headers_data, ["name"]) for row in data[1:]]
    for_csv(file_name, headers_data, rows_data, delimiter_map["Semicolon"], csv.QUOTE_ALL, quote_map["DoubleQuote"], '\\')

def test_case_8():
    file_name = "test8.csv"
    headers_data = data[0]
    rows_data = apply_max_row_length(data[1:], 65535)
    for_csv(file_name, headers_data, rows_data, delimiter_map["Semicolon"], csv.QUOTE_ALL, quote_map["SingleQuote"], '\\')

def for_csv_is_different(file_name, headers, rows, delimiter):
    file_path = os.path.join(output_dir, file_name)
    with open(file_path, mode='w', newline='') as file:
        for row in [headers] + rows:
            line = delimiter.join([str(field) if field != '' else '' for field in row])
            file.write(line + '\n')
    print(f"CSV file generated: {file_name}")

def test_case_9():
    headers_data = ['name', 'age']
    rows_data = [[row[0], row[1]] for row in data[1:]]  # Select only 'name' and 'age'
    rows_data = apply_max_row_length(rows_data, 65535)
    file_name = "test9.csv"
    for_csv_is_different(file_name, headers_data, rows_data, delimiter_map["Semicolon"])

def test_case_10():
    file_name = "test10.csv"
    headers_data = None
    rows_data = [include_columns(row, data[0], ["age"]) for row in data[1:]]
    for_csv(file_name, headers_data, rows_data, delimiter_map["Pipe"], csv.QUOTE_ALL, quote_map["DoubleQuote"], '\\')

def test_case_11():
    file_name = "test11.csv"
    headers_data = data[0]
    rows_data = data[1:]
    for_csv(file_name, headers_data, rows_data, delimiter_map["Pipe"], csv.QUOTE_ALL, quote_map["SingleQuote"], '\\')

def test_case_12():
    file_name = "test12.csv"
    headers_data = None
    rows_data = [include_columns(row, data[0], ["name", "age"]) for row in data[1:]]
    for_csv(file_name, headers_data, rows_data, delimiter_map["Pipe"], csv.QUOTE_ALL, quote_map["DoubleQuote"], '\\')

def test_case_13():
    file_name = "test13.csv"
    headers_data = data[0]
    rows_data = data[1:]
    rows_data = apply_max_row_length(rows_data, 65535)
    for_csv(file_name, headers_data, rows_data, delimiter_map["Auto"], csv.QUOTE_NONE, '', '\\')

def test_case_14():
    file_name = "test14.csv"
    headers_data = data[0]
    rows_data = [exclude_columns(row, data[0], ["name"]) for row in data[1:]]
    for_csv(file_name, headers_data, rows_data, delimiter_map["Auto"], csv.QUOTE_ALL, quote_map["DoubleQuote"], '\\')

def test_case_15():
    file_name = "test15.csv"
    headers_data = None
    rows_data = [include_columns(row, data[0], ["name", "age"]) for row in data[1:]]
    for_csv(file_name, headers_data, rows_data, delimiter_map["Auto"], csv.QUOTE_ALL, quote_map["SingleQuote"], '\\')

def test_case_16():
    file_name = "test16.csv"
    headers_data = data[0]
    rows_data = [include_columns(row, data[0], ["city", "postal_code"]) for row in data[1:]]
    for_csv(file_name, headers_data, rows_data, delimiter_map["Tab"], csv.QUOTE_ALL, quote_map["DoubleQuote"], '\\')

functions = {
    1: test_case_1,
    2: test_case_2,
    3: test_case_3,
    4: test_case_4,
    5: test_case_5,
    6: test_case_6,
    7: test_case_7,
    8: test_case_8,
    9: test_case_9,
    10: test_case_10,
    11: test_case_11,
    12: test_case_12,
    13: test_case_13,
    14: test_case_14,
    15: test_case_15,
    16: test_case_16,
}

for i in functions:
    functions[i]()

print("All CSV test files have been generated!")


