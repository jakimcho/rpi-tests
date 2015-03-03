import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)

base = 11
gpio.setup(base, gpio.OUT)
gpio.output(base, 0)

sleeptime = 1

try:
	while (True):
		gpio.output(base, 1)
		time.sleep(sleeptime)
	
except KeyboardInterrupt:
	gpio.cleanup()
