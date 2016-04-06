#!/usr/bin/env python2.7

import sys

'''
index = 1
while index < len(sys.argv):
	print sys.argv[index],
	index += 1
'''

'''
for argument in sys.argv[1:]:
	print argument,
'''

print ' '.join(sys.argv[1:])
