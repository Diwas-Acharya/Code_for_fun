import socket
s = socket.socket(socket.AF_INET , socket.SOCK_STREAM , 0)
s.connect(("localhost",1028))
while True:

	print("Server => "+s.recv(1024).decode())
	print("client writing = >")
	data = input("")
	s.send(bytes(data,'utf-8'))
