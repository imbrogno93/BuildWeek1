import socket

target = input("Enter the IP address to scan: ")

lowport = 0
highport = 65536

print("Scanning host", target)

for port in range(lowport, highport):
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  status = s.connect_ex((target, port))
  if (status == 0)
    print("Port", port, "- OPEN")
  s.close()