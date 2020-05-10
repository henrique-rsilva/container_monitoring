#!/usr/bin/python
from max6675.max6675 import MAX6675, MAX6675Error
import time

cs_pin = 8
clock_pin = 11
data_pin = 9
units = "c"

thermocouple = MAX6675(cs_pin, clock_pin, data_pin, units)
running = True

while(running):
	try:
		try:
			tc = thermocouple.get()
			print("tc: {} degrees C".format(tc))
			time.sleep(0.25)
		except MAX6675Error as e:
			tc = "Error: "+ e.value
			running = False
			print("tc: {}".format(tc))
			time.sleep(2)
	except KeyboardInterrupt:
		running = False
		print("\nStopped by user\n")
thermocouple.cleanup()
