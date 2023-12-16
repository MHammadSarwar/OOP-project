from bs4 import BeautifulSoup
def gettoken():
    with open('files/output.html', 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Create a BeautifulSoup object
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find the input element with name="sesskey" and get its value
    sesskey_element = soup.find('input', {'name': 'sesskey'})

    if sesskey_element:
        sesskey_value = sesskey_element.get('value')
        print("sesskey value:", sesskey_value)
        return sesskey_value
    else:
        print("sesskey not found in the HTML content.")
