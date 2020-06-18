import socket
s = socket.socket(socket.AF_INET , socket.SOCK_STREAM , 0)
s.bind(("localhost",1028))
s.listen(3)
conn , addr = s.accept()
print("Your friend is online with address ",addr)
n = 1
while True:
	if n == 1:
		data = "welcome to diwas server"
	else:
		print("server writing => ")
		data = input("")
	n = n+1
	conn.send(bytes(data,'utf-8'))
	print("client => "+conn.recv(1024).decode())
	
	
	
	
	
	