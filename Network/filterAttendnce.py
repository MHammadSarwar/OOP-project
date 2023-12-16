import os
from bs4 import BeautifulSoup

def extract_visible_text(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Find all elements containing visible text
    visible_elements = soup.find_all(string=True)
    
    # Extract the visible text
    visible_text = ' '.join(filter(lambda x: x.strip(), visible_elements))
    
    return visible_text

# Loop through HTML files with .CRUDE extension
for filename in os.listdir("files"):
    if filename.endswith(".CRUDE"):
        with open(os.path.join("files", filename), 'r', encoding='utf-8') as file:
            html_content = file.read()
            visible_text = extract_visible_text(html_content)
            
            # Save the visible text content with the same filename and .txt extension
            with open(f"files/{filename}.DISTILLED", 'w', encoding='utf-8') as output_file:
                output_file.write(visible_text)
