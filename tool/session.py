
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
    cv = ''  # holds the cookie value returned by the server
    r = s.post(url, data=login_data)

    for c in s.cookies:
        cv += c.value
    
    print("\nSession is active. Cookie value is: " + cv)
    input("Press Enter to terminate process")
