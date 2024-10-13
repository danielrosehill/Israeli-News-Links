import os
import json

input_folder = os.getcwd()
output_folder = os.path.join(input_folder, "URLs-only")


os.makedirs(output_folder, exist_ok=True)


def extract_urls_from_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as json_file:
        try:
            data = json.load(json_file)
        except json.JSONDecodeError:
            print(f"ERROR: Could not parse JSON in file {file_path}")
            return set()

        urls = set()  

        if isinstance(data, list):
  
            for entry in data:
                if isinstance(entry, dict) and "Website" in entry:
                    urls.add(entry["Website"])
        elif isinstance(data, dict):
       
            for key, value in data.items():
                if isinstance(value, list):
                    for entry in value:
                        if isinstance(entry, dict) and "Website" in entry:
                            urls.add(entry["Website"])
        else:
            print(f"WARNING: Unexpected JSON structure in file {file_path}")

    return urls


def save_urls_to_file(urls, output_path):

    urls_string = ",".join(urls)


    with open(output_path, 'w', encoding='utf-8') as output_file:
        json.dump(urls_string, output_file)


for root, _, files in os.walk(input_folder):

    if root == output_folder:
        continue

    for file in files:
        if file.endswith(".json"):
            input_file_path = os.path.join(root, file)
            output_file_path = os.path.join(output_folder, file)

       
            urls = extract_urls_from_json_file(input_file_path)

        
            if urls:
                save_urls_to_file(urls, output_file_path)

print("URL extraction completed.")
