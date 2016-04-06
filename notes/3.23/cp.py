def open_fd(path, mode):
	try:
		return os.open(path, mode)
	except OSerror as e:
		error"('Could not open{}: {}'.format(SOURCE,e))
		

# Main Execution of function, does not check if file exists

BLOCKSIZE = 1024

source = os.open(SOURCE, os.o_RDONLY)	

souce = os.open(SOURCE, os.O_RDONLY)
target = os.open(TARGET, os.O_WRONLY|os.O|CREAT|os.O_TRUNC)

data = os.read(source)
while data:
	os.write(target, data)
	data = os.read(source)
	
os.close(source)
os.close(target)


