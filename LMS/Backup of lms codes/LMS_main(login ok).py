import requests
from bs4 import BeautifulSoup
from sessionkey import gettoken

session = requests.Session()

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control": "no-cache",
    "Sec-Ch-Ua": "\"Chromium\";v=\"116\", \"Not)A;Brand\";v=\"24\", \"Opera GX\";v=\"102\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "Windows",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 OPR/102.0.0.0",
}


def get_csrf_token():
    try:
        response = session.get("https://lms.nust.edu.pk/portal/login/index.php", headers=headers)
        response.raise_for_status()

        print("GET request to LMS was successful.")
        login_soup = BeautifulSoup(response.text, 'html.parser')
        csrf_token = login_soup.find('input', {'name': 'logintoken'})['value']
        print("CSRF Token:", csrf_token)
        return csrf_token

    except requests.RequestException as e:
        print(f"GET request to LMS failed: {e}")
        return None


def login(username, password):
    csrf_token = get_csrf_token()

    if csrf_token:
        login_url = "https://lms.nust.edu.pk/portal/login/index.php"
        login_payload = {
            'anchor': '',
            'logintoken': csrf_token,
            'username': username,
            'password': password
        }

        try:
            login_response = session.post(login_url, data=login_payload, headers=headers)
            login_response.raise_for_status()

            print("Login successful!")

            # Save the HTML content to a file
            with open('files/output.html', 'w', encoding='utf-8') as file:
                file.write(login_response.text)

            print("HTML content saved to 'files/output.html'")
            # Add further processing or navigate to other pages after successful login.
            # ...

        except requests.RequestException as e:
            print(f"Login request failed: {e}")

# Example usage:
username = "arehman.bee22seecs"
password = "Okok.ok123"
login(username, password)
"""
soup = BeautifulSoup(html_content, 'html.parser')

# Find the input element with name="sesskey" and get its value
sesskey_value = soup.find('input', {'name': 'sesskey'}).get('value')
print(session.cookies)"""



url = 'https://lms.nust.edu.pk/portal/lib/ajax/service.php'

# Specify the parameters
params = {
    'sesskey': gettoken(),
    'info': 'core_course_get_enrolled_courses_by_timeline_classification'
}

# Specify the payload
payload = {
    'index': 0,
    'methodname': 'core_course_get_enrolled_courses_by_timeline_classification',
    'args': {
        'offset': 0,
        'limit': 0,
        'classification': 'all',
        'sort': 'fullname',
        'customfieldname': '',
        # Add other required parameters here
    }
}

# Make the POST request
response = requests.post(url, params=params, json=payload)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Print the response content
    print(response.json())
else:
    print(f"Error: Unable to fetch data. Status code: {response.status_code}")

"""
lms_main=session.get("https://lms.nust.edu.pk/portal/my/",headers=headers)
if lms_main.status_code == 200:
    # Write the HTML content to a file
    output_file_path = 'files/lms.html'
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(lms_main.text)
    print(f"Page content saved to {output_file_path}.")
else:
    print(f"Error: Unable to fetch the page. Status code: {lms_main.status_code}")"""