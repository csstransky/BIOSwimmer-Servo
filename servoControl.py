#!/usr/bin/python
# importing csv module 
import csv 
import math
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

x1 = float (fields[0])
y1 = float (fields[1])
angcom = float (fields[2])
x2 = float (fields[3])
y2 = float (fields[4])

print (x1)
print (x2)
print (angcom)
print (y1)
print (y2)
dx = x1-x2
dy = y1-y2

distance = math.sqrt((dx*dx)+(dy*dy))
print (dx)
print (dy)
print (distance)
ang = math.atan(dx/dy)/(math.pi)*180
print (ang)

if dx == 0:
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
    moveAng = 360 + moveAng
else:
    moveAng = moveAng
print (moveAng)
angle = float (moveAng)
duty = float(angle/180)
print (duty)
GPIO.output(servoPIN,True)
pwm.ChangeDutyCycle(12.5)
sleep(0.865*(duty))


pwm.stop()
GPIO.cleanup()

