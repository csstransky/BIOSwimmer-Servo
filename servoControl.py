#!/usr/bin/python
# importing csv module 
import csv 
import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
servoPIN = 11
GPIO.setup(servoPIN, GPIO.OUT)
pwm=GPIO.PWM(servoPIN, 50)
pwm.start(0)

  
# csv file name 
filename = "~/shared/bioswimmer_file.txt"
  
# initializing the titles and rows list 
fields = [] 
rows = [] 
  
# reading csv file 
with open(filename, 'r') as csvfile: 
    # creating a csv reader object 
    csvreader = csv.reader(csvfile) 
      
    # extracting field names through first row 
    fields = csvreader.next() 
  
    # extracting each data row one by one 
    for row in csvreader: 
        rows.append(row) 
angle = 
  duty = angle/18+2
  GPIO.output(servoPIN,True)
  pwm.ChangeDutyCycle(duty)
  sleep(1)
  GPIO.output(servoPIN,False)
  pwm.ChangeDutyCycle(0)

pwm.stop()
GPIO.cleanup()

