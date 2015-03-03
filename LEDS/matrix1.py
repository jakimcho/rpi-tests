# anodes - pins: 1 - 12; 2 - 16; 3 - 22pin
# cathodes - pins: 1 - 7pin; 2 - 11pin; 3 -15pin

import RPi.GPIO as gpio
import time

sleeptime = 0.2
gpio.setmode(gpio.BOARD)

# Setting the cathodes
cathodes = [7, 11, 15]

for cathode in cathodes:
	gpio.setup(cathode, gpio.OUT)
	gpio.output(cathode, 0)

# Setting the anodes
anodes = [12, 16, 22]

for anode in anodes:
	gpio.setup(anode, gpio.OUT)
	gpio.output(anode, 0)

try:
	while (True):
		gpio.output(anodes[1], 1)
		gpio.output(cathodes[0], 1)
		gpio.output(cathodes[1], 0)
		gpio.output(cathodes[2], 1)

		time.sleep(sleeptime)

		gpio.output(anodes[0], 1)
		gpio.output(anodes[1], 0)
		gpio.output(anodes[2], 1)

		gpio.output(cathodes[0], 0)
		gpio.output(cathodes[1], 1)
		gpio.output(cathodes[2], 0)

		time.sleep(sleeptime)

		gpio.output(anodes[0], 0)
		gpio.output(anodes[1], 0)
		gpio.output(anodes[2], 0)

		gpio.output(cathodes[0], 0)
		gpio.output(cathodes[1], 0)
		gpio.output(cathodes[2], 0)

		time.sleep(sleeptime)

		gpio.output(anodes[0], 1)
		gpio.output(anodes[1], 1)
		gpio.output(anodes[2], 0)

		gpio.output(cathodes[0], 1)
		gpio.output(cathodes[1], 0)
		gpio.output(cathodes[2], 1)

		time.sleep(sleeptime)

		gpio.output(anodes[0], 0)
		gpio.output(anodes[1], 0)
		gpio.output(anodes[2], 0)

		gpio.output(cathodes[0], 0)
		gpio.output(cathodes[1], 0)
		gpio.output(cathodes[2], 0)
		
except KeyboardInterrupt:
	gpio.cleanup()

