import re
import json

def extract_attribute_value_from_logs(log_file_path, attribute):
    # Pattern to match JSON starting with { and ending with }, handling nested structures
    values = []

    with open(log_file_path, 'r') as file:
        for line_number, line in enumerate(file, 1):
            try:
                match = re.search(r'\{.*\}', line)
                if match:
                    parsed_json = json.loads(match.group(0))
                    values.append(parsed_json.get(attribute, None))
            except json.JSONDecodeError:
                continue
    return values

log_file = 'sample.log'
attribute_name = 'user_id'

values = extract_attribute_value_from_logs(log_file, attribute_name)
for value in values:
    print(value)
