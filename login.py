import requests
from csrf import csrf
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

def login():
    csrf_token,session=csrf()
    login_payload = {
    'csrf_token': csrf_token,
    'login': 'arehman.bee22seecs',
    'password': 'Eesucks80085',
    'redirect':"https://qalam.nust.edu.pk/student/dashboard",
    }
    response = session.post("https://qalam.nust.edu.pk/web/login",data=login_payload, headers=login_headers)
    if response.status_code == 200:
        print("Login was successful.")
        return session
    else:
        print(f"Login failed with status code {response.status_code}.")
        return 0