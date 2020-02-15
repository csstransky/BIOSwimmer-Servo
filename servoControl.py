#!/usr/bin/python

import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
servoPIN = 11
GPIO.setup(servoPIN, GPIO.OUT)
pwm=GPIO.PWM(servoPIN, 50)
pwm.start(0)
print("start") 
def SetAngle(angle):
        duty = angle/18+2
        GPIO.output(servoPIN,True)
        print("test1")
        pwm.ChangeDutyCycle(duty)
        sleep(1)
        GPIO.output(servoPIN,False)
        print("test2")
        pwm.ChangeDutyCycle(0)
SetAngle(100)
print ("stop")
pwm.stop()
GPIO.cleanup()

