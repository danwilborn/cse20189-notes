
import os
import socket
import sys

# Constants

ADDRESS = '127.0.0.1'
PROGRAM = os.path.basename(sys.argv[0])

# Echo Client


for PORT in (9300, 9399):
	try:
		client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Allocate TCP socket
		client.connect((ADDRESS, PORT))                             # Connect to server with ADDRESS and PORT
	except socket.error:
		pass


stream = client.makefile('w+')                              # Create file object from socket



while data:
    
	data   = sys.stdin.readline()     # Read from STDIN

	# Send STDIN to Server
	stream.write(data)
	stream.flush()

	# Read from Server to STDOUT
	data = stream.readline()
	sys.stdout.write(data)

	# Read from STDIN
	data = sys.stdin.readline()
