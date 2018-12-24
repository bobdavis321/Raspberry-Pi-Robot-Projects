# PCA9685 Servo controller for 6DOF arm
#
# WERTYU = increase servo 1-5
# ASDFGH = Center servo 1-5
# ZXCVBN = Decrease servo 1-5
# Range is 2.5=0, 7.5=90, 12.5=180
# q=quit

# import curses and GPIO
import curses
import RPi.GPIO as GPIO
import time
# GPIO.setwarnings(False)
from SunFounder_PCA9685 import Servo

# Turn on instant key response
key = curses.initscr()
curses.cbreak()
key.keypad(1)
key.nodelay(1)

# Set default positions
pos1=90
pos2=90
pos3=90
pos4=90
pos5=90
pos6=90

# Write data to servos
myservo = []
for i in range(0,6):
        myservo.append(Servo.Servo(i))  # channel 1
        Servo.Servo(i).setup()
        print 'myservo%s'%i

while True:
    char = key.getch()
    if char == ord('q'):
        break
    elif char == ord('w'):
        if (pos1>20): pos1=pos1-10
    elif char == ord('e'):
        if (pos2>20): pos2=pos2-10
    elif char == ord('r'):
        if (pos3>20): pos3=pos3-10
    elif char == ord('t'):
        if (pos4>20): pos4=pos4-10
    elif char == ord('y'):
        if (pos5>20): pos5=pos5-10
    elif char == ord('u'):
        if (pos6>20): pos6=pos6-10


    elif char == ord('z'):
        if (pos1<160): pos1=pos1+10
    elif char == ord('x'):
        if (pos2<160): pos2=pos2+10
    elif char == ord('c'):
        if (pos3<160): pos3=pos3+10
    elif char == ord('v'):
        if (pos4<160): pos4=pos4+10
    elif char == ord('b'):
        if (pos5<160): pos5=pos5+10
    elif char == ord('n'):
        if (pos6<160): pos6=pos6+10

    elif char == ord('a'):
        pos1=90
    elif char == ord('s'):
        pos2=90
    elif char == ord('d'):
        pos3=90
    elif char == ord('f'):
        pos4=90
    elif char == ord('g'):
        pos5=90
    elif char == ord('h'):
        pos6=90
        
   #     for i in range(0, 180, 5):
    #            print i
    #for channel in range(0, 6):
    myservo[0].write(pos1)
    myservo[1].write(pos2)
    myservo[2].write(pos3)
    myservo[3].write(pos4)
    myservo[4].write(pos5)
    myservo[5].write(pos6)
    #print '   channel%s'%channel
    time.sleep(0.1)

