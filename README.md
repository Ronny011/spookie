# spookie
Cookie spoofing tool and example website

## Website
An example website with simple session management using cookies given to registered users.
Use a back-end MySQL database and insert the user data manually as registration isn't active at the moment.

## Tool
A brute force tool built in python 3.8.x
The tool simply tries to send HTTP requests to the website with unique random session cookie string values.
The values are given in a loop, while each string is inserted as the new default session cookie ("PHPSESSID").
The loop will keep going as long as the website keeps giving a response with the login page URL.
If you have a valid session cookie or if you have logged in successfully (plaintext comparison of username and password),
you will referred to the 'profile' web page.

You can either use the attached 'session' file or open a tab with a registered and logged in user(profile web page).
The aforementioned file will log in with the given data in the 'login_data' dictionary and will run a background active session
and output the cookie value for testing purposes. 
