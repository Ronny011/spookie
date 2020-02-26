
# get cookies - func logs in and pulls session cookie
# fake cookie - func brute forces a possible cookie
# try new cookie - func changes the file name or content and puts inside the directory

import requests
session = requests.Session()
response = session.get('http://localhost/login/new/index.php')
# print(session.cookies.get_dict())
for c in session.cookies:
    print("\nSession cookie information:")
    print("{" + 'name: ' + c.name + ', value :' + c.value + ', domain :' + c.domain + ', path: ' + c.path + "}")
