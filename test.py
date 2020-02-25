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
