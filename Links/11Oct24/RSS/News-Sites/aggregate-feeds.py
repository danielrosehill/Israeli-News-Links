import os
from xml.etree import ElementTree as ET

def merge_opml_files(output_file):
    # Set to store unique feed URLs
    unique_feeds = set()

    # Create the structure of the new OPML file
    root = ET.Element("opml", version="2.0")
    head = ET.SubElement(root, "head")
    title = ET.SubElement(head, "title")
    title.text = "Combined and Sorted OPML Feeds"
    body = ET.SubElement(root, "body")

    # Get the current script's name so it can be ignored
    current_script = os.path.basename(__file__)

    # List to hold feeds for sorting
    all_feeds = []

    # Loop through all the files in the current directory
    for filename in os.listdir('.'):
        if filename.endswith('.opml') and filename != output_file and filename != current_script:
            try:
                # Parse each input OPML file
                tree = ET.parse(filename)
                file_body = tree.find("body")
                
                # Iterate through the outline elements in the body
                for outline in file_body.findall("outline"):
                    feed_url = outline.get("xmlUrl")
                    
                    # Avoid duplicates by checking feed URLs
                    if feed_url not in unique_feeds:
                        unique_feeds.add(feed_url)
                        all_feeds.append(outline)
                    
                print(f"Merged: {filename}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

    # Sort the feeds alphabetically by the 'text' attribute
    all_feeds.sort(key=lambda x: x.get("text", "").lower())

    # Append the sorted feeds to the body
    for feed in all_feeds:
        body.append(feed)

    # Write the merged and sorted result to the output file
    tree = ET.ElementTree(root)
    tree.write(output_file, encoding="UTF-8", xml_declaration=True)

if __name__ == "__main__":
    # Output file for the combined result
    output_file = 'all-feeds.opml'
    
    # Merge and sort the files
    merge_opml_files(output_file)
