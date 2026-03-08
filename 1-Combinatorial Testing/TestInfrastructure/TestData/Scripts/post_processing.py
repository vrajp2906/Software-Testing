def fix_json_structure(dir):
    try:
        with open(dir, 'r') as file:
            content = file.read().strip()
        data = content.replace('{"inner_key":', '').replace('}}', '}')

        with open(dir, 'w') as file:
            file.write(data)
