
# imports
from bs4 import BeautifulSoup as bs
import requests

# constants
url = "http://localhost/login/new/index.php"
name = 'PHPSESSID'

# user credentials
login_data = {
    "username": 'liron',
    "password": '3232',
    "submit": " Login "
}
login_data2 = {
    "username": 'roni',
    "password": '123',
    "submit": " Login "
}

# session
with requests.Session() as s:
    r = s.post(url, data=login_data)

    for c in s.cookies:
        sl += c.value
    
    print("Session is active. Cookie value is: " + sl)