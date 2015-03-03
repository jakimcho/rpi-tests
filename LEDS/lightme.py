import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)

cathode = 12
anode = 7

gpio.setup(anode, gpio.OUT)
gpio.setup(cathode, gpio.OUT)

gpio.output(anode, 0)
gpio.output(cathode, 0)

gpio.output(anode, 1)

time.sleep(5)

gpio.output(cathode, 1)

time.sleep(2)

gpio.cleanup()
