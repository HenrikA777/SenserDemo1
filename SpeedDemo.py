from sense_hat import SenseHat
import time

sense = SenseHat()
speed = 0
p = 0
blue = (0, 0, 255)
sense.clear()


while True:
	acceleration = sense.get_accelerometer_raw()
	x = acceleration['x']
	y = acceleration['y']
	z = acceleration['z']
	
	speed = speed * 0.99
	
	p += 1
  
	if (x > 0.01 or x < -0.01):
	  speed += x
	  
	if (p == 5):
	  print(speed)
	  p = 0
	  sense.clear()
	  if (speed > 2 and speed < 4):
	    sense.set_pixel(5, 5, blue)
	  if (speed > 4 and speed < 8):
	    sense.set_pixel(6, 5, blue)
	  if (speed > 8):
	    sense.set_pixel(7, 5, blue)
	  if (speed < -2 and speed > -4):
	    sense.set_pixel(2, 5, blue)
	  if (speed < -4 and speed > -8):
	    sense.set_pixel(1, 5, blue)
	  if (speed < -8):
	    sense.set_pixel(0, 5, blue)
	  if (speed < 2 and speed > -2):
	    sense.set_pixel(4, 5, blue)
	    sense.set_pixel(3, 5, blue)