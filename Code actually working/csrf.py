import requests
from bs4 import BeautifulSoup
session = requests.Session()
# Define the URL for the GET request
url = "https://qalam.nust.edu.pk"

# Define the headers for the request
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control": "no-cache",
    "Cookie": "session_id=18fec3023a11a4f6ae543bb20be2e3dc1dfa9d5a; frontend_lang=en_US; im_livechat_history=[\"/\"]",
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

response = session.get(url, headers=headers)
if response.status_code == 200:
        print(f"POST request to {url} was successful.")
        print(response.text)
        login_soup = BeautifulSoup(response.text,'html.parser')
        csrf_token = login_soup.find('input', {'name': 'csrf_token'})['value']
        print(csrf_token)
else:
        print(f"POST request to {url} failed with status code {response.status_code}.")

