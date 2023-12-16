import requests
from bs4 import BeautifulSoup
from user_id import getuser_id
from Link_level_filter import get_links
import pandas
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


def save_html(outputfilepath:str,link):
    response=session.get(link,headers=headers)
    if response.status_code==200:
        with open(outputfilepath,'w',encoding="utf-8") as f:
            f.write(response.text)
    else:
        print(f"Login failed with status code {(response.status_code)}.")

#login
username = "arehman.bee22seecs"
password = "Okok.ok123"
login(username, password)

user_id=getuser_id()
url="https://lms.nust.edu.pk/portal/user/profile.php?id="+user_id
print(url)
page_response=session.get(url,headers=headers)
if page_response.status_code==200:
    with open('files/courseslist.html', 'w', encoding='utf-8') as file:
        file.write(page_response.text)
        get_links(file.name)
else:
    print("Failed to get courses")

import csv

with open('files/Links_to_courses.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        flag = int(row['flag'])
        if flag == 0:
            continue
        elif flag == 1:
            payload={'id':row['payload']}
            page_response=session.get(row['links'],headers=headers)
            if page_response.status_code == 200:
                with open(f"files/{row['name']}.html", 'w', encoding="utf-8") as f:
                    f.write(page_response.text)
            else:
                print(f"Login failed with status code {(page_response.status_code)}.")







