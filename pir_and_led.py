#!/usr/bin/python
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(11, GPIO.IN)
GPIO.setup(3, GPIO.OUT)




while True:
	i = GPIO.input(11)
	
	if i == 0:
		print "No Intruders", i
		GPIO.output(3, 0)
		time.sleep(0.1)

	elif i == 1:
		print "INTRUDER DETECTED!!", i
		GPIO.output(3, 1)
		time.sleep(0.1)
