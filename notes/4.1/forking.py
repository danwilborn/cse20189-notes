#!/usr/bin/env python2.7

import os
import signal
import sys
import time


pid = os.fork()
if pid == 0:	# Child
	print '* Child pid: {}, Parent pid: {}'.format(os.getpid(), os.getppid())
	time.sleep(10)
	sys.exit(1)
else:			# Parent
	print '# Child pid: {}, Parent pid: {}'.format(pid, os.getpid())
	os.kill(pid, signal.SIGHUP)
	pid, status = os.wait()
	print '# Child pid: {} exited with status {}'.format(pid, status >> 
	8)
