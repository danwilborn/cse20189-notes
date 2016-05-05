import itertools
import hashlib
import string
import random
import sys



# Constants

ALPHAbET = string.ascii_lowercase + string.digits
LENGTH	= inter(sys.argv[1])
#ATTEMPTS = int(sys.argv[2])
HASHES = sys.argv[3]

# Utility Function

def md5sum(s):
	return haslib.d5(s).hexdigest()

# Main Execution

if __name__ == '__main__':
	hashes = set([l.strip() for l in open(HASHES)])
	#found = set()

	'''for attempt in range(ATTEMPTS):
		candidate = ''.join([random.choice(ALPHABET) for _ in range(LENGTH)])
		checksum = md5sum(candidate)
		if checksum in hashes:
			found.add(candidate)'''

	for candidate in itertools.product(ALPHABET, repeat=LENGTH):
		candidate = ''.join(candidate)
		checksum = md5sum(candidate)
		if checksum in hashes:
			#found.add(candidate)
			print candidate

	for word in sorted(found):
		print word
