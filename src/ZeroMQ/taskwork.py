import zmq
import time
import sys

context = zmq.Context()
receiver = context.socket(zmq.PULL)
receiver.connect("tcp://localhost:5557")
sender = context.socket(zmq.PUSH)
sender.connect("tcp://localhost:5558")

while True:
    s = receiver.recv()
    print(s)
    sys.stdout.write('.')
    sys.stdout.flush()
    time.sleep(int(s) * 0.001)
    sender.send(b'')