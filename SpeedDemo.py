from sense_hat import SenseHat
import time

sense = SenseHat()
speed = 0
p = 0
#red not blue xD
blue = (255, 0, 0)
sense.clear()


while True:
	acceleration = sense.get_accelerometer_raw()
	x = acceleration['x']
	
	speed = speed * 0.98
	if (speed < 1 and speed > -1):
		speed = speed * 0.9
	
	p += 1
  
	if (x > 0.2 or x < -0.2):
	  speed += x
	  
	if (p == 1):
	  print(speed)
	  p = 0
	  sense.clear()
	  if (speed > 0.5 and speed < 1):
	    sense.set_pixel(2, 5, blue)
	  if (speed > 1 and speed < 2):
	    sense.set_pixel(1, 5, blue)
	  if (speed > 2):
	    sense.set_pixel(0, 5, blue)
	  if (speed < -0.5 and speed > -1):
	    sense.set_pixel(5, 5, blue)
	  if (speed < -1 and speed > -2):
	    sense.set_pixel(6, 5, blue)
	  if (speed < -2):
	    sense.set_pixel(7, 5, blue)
	  if (speed < 0.5 and speed > -0.5):
	    sense.set_pixel(4, 5, blue)
	    sense.set_pixel(3, 5, blue)