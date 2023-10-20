import http.client, requests

host = input("Inserire host/IP: ")
port = input("Inserire porta [range 0-65535] (default: 80): ")
path = input("Inserire path: ")

if (port == ""):
  port = 80

methods = ["GET", "POST", "PUT", "PATCH", "DELETE", "HEAD", "OPTIONS", "CONNECT"]

try:
  for method in methods:
    connection = http.client.HTTPConnection(host, port)
    connection.request(method, path)
    response = connection.getresponse()
    if response.status == 200:
      print(" " + method + "---> Abilitato")
    else:
      print(" " + method + "---> Non abilitato")
    connection.close()
except ConnectionRefusedError:
  print("Connessione fallita")