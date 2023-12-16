from bs4 import BeautifulSoup
def getuser_id():
    with open('files/output.html', 'r', encoding='utf-8') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')
    message_user_button = soup.find('a', {'id': 'message-user-button'})

    if message_user_button:
        data_userid_value = message_user_button.get('data-userid')
        print("data-userid value:", data_userid_value)
        return data_userid_value
    else:
        print("data-userid attribute not found in the HTML content.")