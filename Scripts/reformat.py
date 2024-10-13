import os
import csv
import json

folder_path = os.getcwd()

json_output_folder = os.path.join(folder_path, 'JSON')
os.makedirs(json_output_folder, exist_ok=True)

def csv_to_json(csv_file, json_file, array_name):
    json_data = {array_name: []}  

    with open(csv_file, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        
        for row in csv_reader:
  
            json_data[array_name].append({
                'Publication Name': row['Publication_Name'],
                'Website': row['Website']
            })


    with open(json_file, mode='w', encoding='utf-8') as outfile:
        json.dump(json_data, outfile, indent=4)


for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):

        csv_file_path = os.path.join(folder_path, filename)
        json_file_path = os.path.join(json_output_folder, filename.replace('.csv', '.json'))
        country_name = filename.replace('.csv', '')

        array_name = f'{country_name} News Websites'

        csv_to_json(csv_file_path, json_file_path, array_name)

print("CSV files have been successfully converted to JSON and saved in the 'JSON' folder.")
