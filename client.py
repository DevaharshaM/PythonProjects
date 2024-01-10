import socket

Host_IP = "192.168.1.2"
Port = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((Host_IP, Port))

while True:
	message = s.recv(2048)
	print(f"Message recieved: {message}")
	s.send(bytes("Hello from client","utf-8"))
s.close()