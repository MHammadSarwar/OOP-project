from bs4 import BeautifulSoup
def get_links(input_file):
    # Read the HTML content from the file
    with open(input_file, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Parse the HTML content using Beautiful Soup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all the 'a' (anchor) tags in the HTML
    all_links = soup.find_all('a')

    # Extract links and write them to a text file
    output_file = input_file+'.links'
    with open(output_file, 'w', encoding='utf-8') as links_file:
        for link in all_links:
            href = link.get('href')
            if href:
                links_file.write(href + '\n')

    print(f"Links extracted from {input_file} and saved to {output_file}.")
