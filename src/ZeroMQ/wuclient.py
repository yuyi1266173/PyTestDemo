import sys
import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)
print("Collecting updates from weather server...")
socket.connect("tcp://localhost:5556")

zip_filter = sys.argv[1] if len(sys.argv) > 1 else "10001"
print("zip_filter:",zip_filter)

if isinstance(zip_filter, bytes):
    zip_filter = zip_filter.decode('ascii')

# socket.setsockopt_string(zmq.SUBSCRIBE, zip_filter)
total_temp = 0

for update_nbr in range(5):
    string = socket.recv_string()
    zipcode, temperature, relhumidity = string.split()
    print("{}---{}".format(update_nbr, temperature))
    total_temp += int(temperature)
print(total_temp)
print("Average temperature for zipcode '%s' was %0.2fF" % (zip_filter, total_temp / (update_nbr + 1)))