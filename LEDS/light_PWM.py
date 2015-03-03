import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)
anode = 7

gpio.setup(anode, gpio.OUT)

pwm = gpio.PWM(anode,50)
pwm.start(0)

try:
	while True:
		for i in range (100):
			pwm.ChangeDutyCycle(i)
			time.sleep(0.02)
		for i in range (100):
			pwm.ChangeDutyCycle(100 - i)
			time.sleep(0.02)
except KeyboardInterrupt:
	pass

pwm.stop()
gpio.cleanup()
