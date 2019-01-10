# PCA9685 Servo controller for 16DOF humanoid
#
# 01234567890 = select servo 0-15
# Z = Center all servos
# -,+ = Decrease, increase servo 
# Range is 20-90-160
# q=quit

import curses
import RPi.GPIO as GPIO
import time
from SunFounder_PCA9685 import Servo

# Turn on instant key response
key = curses.initscr()
#curses.cbreak()
key.keypad(1)
key.nodelay(1)

# Set default positions
s=[90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90]
sservo=0
r=[90,70,70,90,90,90,90,90,90,90,90,90,90,90,90,90]
l=[90,90,90,90,90,110,110,90,90,90,90,90,90,90,90,90]
w=[90,90,90,90,90,90,90,90,70,120,120,20,90,90,90,90]
f=[90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90]

# Set up servos
myservo = []
for i in range(0, 16):
        myservo.append(Servo.Servo(i))  # channel 1
        Servo.Servo(i).setup()

while True:
    char = key.getch()
    if char == ord('q'):
        break
    elif char == ord('1'):
        sservo=1
    elif char == ord('2'):
        sservo=2
    elif char == ord('3'):
        sservo=3
    elif char == ord('4'):
        sservo=4
    elif char == ord('5'):
        sservo=5
    elif char == ord('6'):
        sservo=6
    elif char == ord('7'):
        sservo=7
    elif char == ord('8'):
        sservo=8
    elif char == ord('9'):
        sservo=9
    elif char == ord('0'):
        sservo=0
    elif char == ord('!'):
        sservo=11
    elif char == ord('@'):
        sservo=12
    elif char == ord('#'):
        sservo=13
    elif char == ord('$'):
        sservo=14
    elif char == ord('%'):
        sservo=15
    elif char == ord(')'):
        sservo=10

    elif char == ord('r'):
        for i in range (0,16):
          s[i]=r[i]
    elif char == ord('l'):
        for i in range (0,16):
          s[i]=l[i]

    elif char == ord('w'):
        for i in range (0,16):
          s[i]=w[i]

        
    # Zero servos (90 degrees)
    elif char == ord('z'):
       for i in range (0,16):
           s[i]=90

    elif char == ord('-'):
        for i in range (0,16):
          if (sservo==i):
            if (s[i]>20) : s[i]=s[i]-2
                   
    elif char == ord('='):
        for i in range (0,16):
          if (sservo==i):
            if (s[i]<120) : s[i]=s[i]+2
              
    print sservo
    # Send info to servos
    for i in range (0,16):
            myservo[i].write (s[i])
  
    time.sleep(0.1)

# Close down properly
curses.nocbreak()
key.keypad(0)
curses.echo()
curses.endwin()
# GPIO.cleanup()
