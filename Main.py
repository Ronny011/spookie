
#  [✓] get cookies - func logs in and pulls session cookie
#  [ ] fake cookie - func brute forces a possible cookie
#  [ ] try new cookie - func changes the file name or content and puts inside the directory

from bs4 import BeautifulSoup as bs
import requests
login_data = {
    "username": 'liron',
    "password": '3232',
    "submit": " Login "
}
with requests.Session() as s:
    url = "http://localhost/login/new/index.php"
    r = s.post(url, data=login_data)
    t = s.get(url)
    soup = bs(r.content, 'html.parser')
    soup = bs(t.content, 'html.parser')
    print("\n")
    flag = 1
    #print(soup)
    print(r.url)
    print(t.url)
    #str1 =
    #print(s.cookies)
