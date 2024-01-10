import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 8080))
s.listen(5)
clientSocket, address = s.accept()
print(f"Conection established from address {address}")
	
while True:
	clientSocket.send(bytes("Welcome to the server!!!", "utf-8"))
	Message = clientSocket.recv(2048)
	print(f"Message recieved: {Message}")
clientSocket.close()