import os
import json
import glob

folder_path = os.getcwd()
json_files = glob.glob(os.path.join(folder_path, '*.json'))

combined_data = []

for json_file in sorted(json_files):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
        combined_data.append(data)
output_file = os.path.join(folder_path, 'all-countries.json')
with open(output_file, 'w', encoding='utf-8') as outfile:
    json.dump(combined_data, outfile, indent=4)

print(f"All JSON files have been successfully combined into {output_file}.")
