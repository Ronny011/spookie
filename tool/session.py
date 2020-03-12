
# imports
from bs4 import BeautifulSoup as bs
import requests

# constants
url = "http://localhost/login/new/index.php"
name = 'PHPSESSID'

# user credentials
login_data = {
    "username": 'user1',
    "password": 'password',
    "submit": " Login "
}
login_data2 = {
    "username": 'user2',
    "password": 'password2',
    "submit": " Login "
}

# session
with requests.Session() as s:
    cv = ''  # holds the cookie value returned by the server
    r = s.post(url, data=login_data)

    for c in s.cookies:
        cv += c.value
    
    print("\nSession is active. Cookie value is: " + cv)
    input("Press Enter to terminate process")
