#!/usr/bin/python

import socket

server = socket.socket(
		socket.AF_INET, # IPv4
		socket.SOCK_STREAM) # TCP

server.bind(('0.0.0.0', 9999))
server.listen(0)

client, address = server.accept()
print 'Connection from', address

stream = client.makefile('w+')
data = stream.readline().rstrip()
while data:
	print data
	data = stream.readline().rstrip()

stream.write('HTTP/1.0 200 OK')
