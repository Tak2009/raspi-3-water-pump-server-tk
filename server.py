# server side
import socket
import pickle
import time
import motor as motor
import config as conf

# https://note-tech.com/python_socket_programming_udp/#toc2

UDP_IP = conf.UDP_IP
UDP_PORT = conf.UDP_PORT
address = (UDP_IP, UDP_PORT)

# create a socket. IPv4 and UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Socket created")
sock.bind(address)

while True:
    try:
        print("Waiting data")
        pickled_data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
#         print('recieved data: ' + str(pickled_data))
#         print('recieved data type: ' + str(type(pickled_data)))
        data = pickle.loads(pickled_data)
#         print('restored pickled data: ' + str(data))
#         print('restored pickled data type: ' + str(type(data)))
        state = data.get("state")
        watering_duration = data.get("watering_duration")
        pause = data.get("pause")
        if  state == "DRY":
                print('Pump on for ' + str(watering_duration) +' seconds')
                motor.motor("on")               
                time.sleep(watering_duration)
                print('Pump turning off, waiting for ' + str(pause) +' seconds')
                motor.motor("off")
                time.sleep(pause)
                print("Waiting for the next data from client")
        else:
            print('Closing socket now: state is ' + str(data.get("state")))
            sock.close()
            motor.clean_gpio()
            print("Closed")
            break
    except KeyboardInterrupt:
        sock.close()
        motor.clean_gpio()
        print("Ctr-C by KeyboardInterrupt")
        break
