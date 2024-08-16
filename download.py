#!/usr/bin/python3
#!/coded/by/@DARK_LMNx9

# JOIN - https://t.me/DARK_TEAM_LMNx9

import os,sys,requests,json,bs4
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
os.system('clear');os.system('xdg-open https://t.me/bcspteam')

url = "https://savetik.co/api/ajaxSearch"
link = input("Enter Your Link : ")
os.system("clear")
payload = f"q={link}&lang=en"

session = requests.Session()
user_agent = UserAgent().random

headers = {
    'User-Agent': user_agent,
    'Content-Type': "application/x-www-form-urlencoded",
    'sec-ch-ua': "\"Google Chrome\";v=\"113\", \"Chromium\";v=\"113\", \"Not-A.Brand\";v=\"24\"",
    'dnt': "1",
    'sec-ch-ua-mobile': "?1",
    'x-requested-with': "XMLHttpRequest",
    'sec-ch-ua-platform': "\"Android\"",
    'origin': "https://savetik.co",
    'sec-fetch-site': "same-origin",
    'sec-fetch-mode': "cors",
    'sec-fetch-dest': "empty",
    'referer': "https://savetik.co/en2",
    'accept-language': "ar,en-US;q=0.9,en;q=0.8"
}

response = session.post(url, data=payload, headers=headers)

if response.status_code == 200:
    try:
        data = response.json()
        soup = BeautifulSoup(data['data'], 'html.parser')
        links = soup.find_all('a', class_='tik-button-dl')
        if len(links) >= 2:
            link = links[1]['href']
            print(link)
        else:
            print("Error: No valid download link found.")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
else:
    print(f"Request failed with status code {response.status_code}")
