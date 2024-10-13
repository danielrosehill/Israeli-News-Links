import csv


input_file = 'links_1.csv'
output_file = 'links_2.csv'

def generate_google_search_url(website_url, keyword="Israel"):
    return f"https://www.google.com/search?q=site:{website_url}+{keyword}"

with open(input_file, mode='r', newline='', encoding='utf-8') as infile, \
     open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
    
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    

    for row in reader:
        if len(row) == 3:  # Ensure the row has 3 values
            website_url = row[2]
            google_search_link = generate_google_search_url(website_url)
            row.append(google_search_link)
        writer.writerow(row)

print(f"Updated CSV saved as {output_file}")
