
# get cookies - func logs in and pulls session cookie
# fake cookie - func brute forces a possible cookie
# try new cookie - func changes the file name or content and puts inside the directory

import requests
from bs4 import BeautifulSoup
from requests import Session
from bs4 import BeautifulSoup as bs


with Session() as s:
    url="http://localhost/login/new/index.php"
    login_data = {
        "username": 'roni',
        "password": '123',
        "submit": " Login "
    }
    print("some cookie")
    a=s.post(url)
    print(a.cookies)
    print(a.content)
    r = s.post(url, data=login_data)
    bs_content = bs(r.content, "html.parser")

    s.post("http://localhost/login/new/", login_data)
    home_page = s.get("http://localhost/login/new/")
    print(home_page.content)
    print(s.cookies)




    s.cookies.set(value='aoakutiqcmea2bu5gmvjvr',name='PHPSESSID')

    print(s.cookies)
    s.post(url,data=s.cookies)
    home_page2 = s.get("http://localhost/login/new/")
    print(home_page2.content)
