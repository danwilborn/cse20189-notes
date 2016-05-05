


import sys
import work_queue

# Constants

LENGTH	 = int(sys.argv[1])
ATTEMPTS = int(sys.argv[2])
HASHES 	 = sys.argv[3]
TASKS 	 = int(sys.argv[4])
SOURCES  = ('mini-hulk.py', HASHES)
PORT 	 = 8451


# Main Execution

if __name__ == '__main__':
	queue = work_queue.WorkQueue(PORT, name='fury-luke', catalog=True)
	queue.specify_log('mini-fury.log')


	for _ in range(TASKS):
		command = './mini-hulk.py {} {} {}'.format(LENGTH, ATTEMPTS, HASHES)
		task	= work_que.TASK(command)
		
		for source in SOURCES:
			task.specify_file(source, source, work_queue.WORK_QUEUE_INPUT)

		queue.submit(task)
	
	while not queue.empty():
		task = queue.wait()
		if task and task.return_status == 0:
			sys.stdout.write(task.output)
