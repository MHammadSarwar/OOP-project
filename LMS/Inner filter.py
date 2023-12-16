import os
from bs4 import BeautifulSoup


def extract_visible_text(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find the <div> element with id "page_content_inner"
    page_content_inner = soup.find('div', {'id': 'page_content_inner'})

    # Extract the visible text within the specified <div> while preserving formatting
    if page_content_inner:
        visible_text = page_content_inner.get_text()
    else:
        visible_text = ''

    return visible_text


def remove_consecutive_empty_lines(text):
    # Split the text into lines
    lines = text.splitlines()

    # Remove consecutive empty lines
    cleaned_lines = [line for i, line in enumerate(lines) if i == 0 or (line.strip() or lines[i - 1].strip())]

    # Join the cleaned lines
    cleaned_text = '\n'.join(cleaned_lines)

    return cleaned_text


# Specify the directory containing the HTML files with the .CRUDE extension
input_directory = "files"

# Create a directory for the output files if it doesn't exist
output_directory = "files"

# Loop through HTML files with .CRUDE extension
for filename in os.listdir(input_directory):
    if filename.endswith(".CRUDE"):
        with open(os.path.join(input_directory, filename), 'r', encoding='utf-8') as file:
            html_content = file.read()
            visible_text = extract_visible_text(html_content)
            cleaned_text = remove_consecutive_empty_lines(visible_text)

            # Create the output file with the same filename and .LESSCRUDE extension
            output_filename = filename + ".DISTILLED"
            output_path = os.path.join(output_directory, output_filename)
            with open(output_path, 'w', encoding='utf-8') as output_file:
                output_file.write(cleaned_text)
