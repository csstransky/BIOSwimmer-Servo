#!/usr/bin/python
# importing csv module 
import csv 
import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
servoPIN = 11
GPIO.setup(servoPIN, GPIO.OUT)
pwm=GPIO.PWM(servoPIN, 50)
pwm.start(0)

print("start") 
  
# initializing the titles and rows list 
fields = []  
rows = []
# reading csv file 
with open('/home/pi/shared/bioswimmer_file.txt', "r") as csv_file: 
    # creating a csv reader object 
    csv_reader = csv.reader(csv_file) 
      
    # extracting field names through first row 
    fields = csv_reader.next() 
    
    # extracting each data row one by one 
    for row in csv_reader: 
        rows.append(row) 

    print (fields)

angle = 0
duty = 12.5
print ("duty = ")
print(duty)
GPIO.output(servoPIN,True)
pwm.ChangeDutyCycle(2)
sleep(1)
GPIO.output(servoPIN,False)
pwm.ChangeDutyCycle(0)

pwm.stop()
GPIO.cleanup()

