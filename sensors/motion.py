import picamera
import RPi.GPIO as io
import time
io.setmode(io.BOARD)

camera = picamera.PiCamera()
counter = 0
io.cleanup()

detector = 18
led = 22

io.setup(detector, io.IN, pull_up_down=io.PUD_DOWN)
io.setup(led, io.OUT)

print("Test the led")
io.output(led, True)
time.sleep(5)
io.output(led, False)
try:
	print "Enter in the loop"
	while True:
		if (io.input(detector)):
			print ("Motion detected")
			camera.capture("imgs/image" + str(counter) + ".png")
			counter += 1
			io.output(led, True)
			time.sleep(5)
			io.output(led, False)
except KeyboardInterrupt:
	print "Quit"
	io.cleanup()
