#!/usr/bin/python

# Set up libraries and overall settings
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
ang = math.asin(dy / distance)/(math.pi)*180
print (ang)

if x1>0 and y1>0
    ang = ang 
else if x1 >0 and y1<0
    ang = 180+ang
else if x1<0 and y1<0
    ang = 180-ang
else if x1 <0 and y1 > 0 
    ang = 360+ang
