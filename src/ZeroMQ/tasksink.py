import time
import zmq
import sys

context = zmq.Context()
receiver = context.socket(zmq.PULL)
receiver.bind("tcp://*:5558")

s = receiver.recv()
tstart = time.time()

for task_nbr in range(1, 100):
    s = receiver.recv()
    print(s)
    if task_nbr % 10 == 0:
        sys.stdout.write(':')
    else:
        sys.stdout.write('.')
    sys.stdout.flush()
tend = time.time()
print("Total elapsed time: %d msec" % ((tend - tstart) * 1000))