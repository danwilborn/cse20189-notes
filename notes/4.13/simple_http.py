#!/usr/bin/python

import socket

DOMAIN = 'www.example.com'
PORT = 80

address = socket.gethostbyname(DOMAIN)
print address

client = socket.socket(socket.AF_INET)
		socket.AF_INET, # IPv4  
		socket.SOCK_STREAM) # TCP

client.connect((address, PORT))

# Convert file descriptor into file object
stream = client.makefile('w+')

stream.write('GET / HTTP/1.0\r\n\r\n')
stream.flush()

data = stream.readline()
while data:
	print data
	data = stream.readline()
