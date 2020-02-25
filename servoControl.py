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

import math 
x1 = 37.23
y1 = 49.23
angcom = 103.9
x2 = 37.46
y2 = 49.54

dx = x1-x2
dy = y1-y2

distance = math.sqrt((dx*dx)+(dy*dy))
print (dx)
print (dy)
print (distance)
ang = math.atan(dx/dy)/(math.pi)*180
print (ang)

if dx == 0:f
    ang = 0
elif dx < 0 and dy< 0:
    ang =-180+ang
elif dx < 0 and dy >  0: 
    ang = 180-ang
else: 
    ang = ang
print (ang)

moveAng = ang - angcom
print (moveAng)
if moveAng <0:
    moveAng = 360 + fmoveAng
else:
    moveAng = moveAng
print (moveAng)
angle = 90
duty =angle/180
print ("duty = ")
print(duty)
GPIO.output(servoPIN,True)
pwm.ChangeDutyCycle(12.5)
sleep(0.865/4)


pwm.stop()
GPIO.cleanup()

