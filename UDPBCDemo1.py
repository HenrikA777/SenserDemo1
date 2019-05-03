BROADCAST_TO_PORT = 15000
import time
from socket import *
from datetime import datetime
from sense_hat import SenseHat

sense = SenseHat()

s = socket(AF_INET, SOCK_DGRAM)
#s.bind(('', 14593))     # (ip, port)
# no explicit bind: will bind to default IP + random port
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
while True:
    sense.show_message(str(BROADCAST_TO_PORT))
    data = "Current time: " + str(datetime.now()) + "\n" + "Temperatur: " + str(sense.get_temperature) + " Celsius"
    s.sendto(bytes(data, "UTF-8"), ('<broadcast>', BROADCAST_TO_PORT))
    sense.show_message("Done")
    time.sleep(5)