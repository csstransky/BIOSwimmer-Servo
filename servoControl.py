#!/usr/bin/python

import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
servoPIN = 11
GPIO.setup(servoPIN, GPIO.OUT)
pwm=GPIO.PWM(servoPIN, 50)
pwm.start(0)

def SetAngle(angle):
    duty = angle/18+2
    GPIO.output(servoPIN,True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(servoPIN,False)
    pwm.ChangeDutyCycle(0)
SetAngle(90)
pwm.stop()
GPIO.cleanup()

