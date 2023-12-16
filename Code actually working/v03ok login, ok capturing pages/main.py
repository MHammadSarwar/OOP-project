import requests
from bs4 import BeautifulSoup
from encryptor import encrypt
from encryptor import decrypt
session = requests.Session()
# Define the URL for the GET request

url = "https://qalam.nust.edu.pk"

# Define the headers for the request
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control": "no-cache",
    "Pragma": "no-cache",
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
login_headers={
    "Accept": "text/html, application/xhtml+xml, application/xml;q=0.9, image/avif, image/webp, image/apng, */*;q=0.8, application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US, en;q=0.9",
    "Cache-Control": "no-cache",
    "Origin": "https://qalam.nust.edu.pk",
    "Pragma": "no-cache",
    "Referer": "https://qalam.nust.edu.pk",
    "Sec-Ch-Ua": "\"Chromium\";v=\"116\", \"Not)A;Brand\";v=\"24\", \"Opera GX\";v=\"102\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 OPR/102.0.0.0",
    
}

response = session.get(url, headers=headers)
if response.status_code == 200:
        print(f"Get request to {url} was successful.")
        login_soup = BeautifulSoup(response.text,'html.parser')
        csrf_token = login_soup.find('input', {'name': 'csrf_token'})['value']
        print(csrf_token)
        url= "https://qalam.nust.edu.pk/web/login"
        login_payload = {
        'csrf_token': csrf_token,
        'login': 'arehman.bee22seecs',
        'password': 'Eesucks80085',
        'redirect':"https://qalam.nust.edu.pk/student/dashboard",
       }
        login_response = session.post(url, data=login_payload, headers=login_headers)
    
        if login_response.status_code == 200:
            print("Login successful.")
            # You can add further logic here to verify the success of the login.
        else:
            print(f"Login failed with status code {login_response.status_code}.")
           
else:
        print(f"POST request to {url} failed with status code {response.status_code}.")

import concurrent.futures

# Define a function to make a GET request to a URL
with open("files/links.txt", "r") as file:
    urls_to_fetch = [line.strip() for i, line in enumerate(file.readlines()) if i % 2 == 1]

# Define a function to make a GET request to a URL
def fetch_url(url):
    response = session.get(url, headers=headers)
    if response.status_code == 200:
        filename = url.split("/")[-1]
        with open(f"files/{filename}.CRUDE", "w", encoding="utf-8") as html_file:
            html_file.write(response.text)
    else:
        return f"GET request to {url} failed with status code {response.status_code}."

# Create a ThreadPoolExecutor to fetch URLs concurrently
with concurrent.futures.ThreadPoolExecutor() as executor:
    results = list(executor.map(fetch_url, urls_to_fetch))

# Process the results (HTML content or error messages)
for result in results:
    print(result)