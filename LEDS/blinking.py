import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)

gpio.setup(12, gpio.OUT)
gpio.setup(11, gpio.OUT)

gpio.output(12, 0)
gpio.output(11, 0)


i = 0
while (i < 10):
	
	time.sleep(0.1)
	gpio.output(12, 1)

	time.sleep(0.15)
	gpio.output(12, 0)
	
	time.sleep(0.2)
        gpio.output(11, 1)

        time.sleep(0.1)
        gpio.output(11, 0)	
	
	i = i + 1

gpio.cleanup()
