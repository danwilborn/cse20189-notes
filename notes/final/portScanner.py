
import os
import socket
import sys

# Constants

ADDRESS = 'student00.cse.nd.edu'

# Echo Client

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Allocate TCP socket
for PORT in range(9300, 9399):
	try:
		client.connect((ADDRESS, PORT))                             # Connect to server with ADDRESS and PORT
		stream = client.makefile('w+')                              # Create file object from socket
		data   = sys.stdin.readline()                               # Read from STDIN
		while data:
			stream.flush()

			# Read from Server to STDOUT
			data = stream.readline()

			# Read from STDIN
			data = sys.stdin.readline()
	except socket.error:
		pass



