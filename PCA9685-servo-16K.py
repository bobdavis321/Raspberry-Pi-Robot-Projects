# PCA9685 Servo controller for 6DOF arm
#
# 1234567890 = select servo 1-10
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
s1=90
s2=90
s3=90
s4=90
s5=90
s6=90
s7=90
s8=90
s9=90
s10=90
s11=90
s12=90
s13=90
s14=90
s15=90
s16=90

sservo=1

# Set up servos
myservo = []
for i in range(0,16):
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
    elif char == ord('!'):
        sservo=9
    elif char == ord('@'):
        sservo=10
    elif char == ord('#'):
        sservo=11
    elif char == ord('$'):
        sservo=12
    elif char == ord('%'):
        sservo=13
    elif char == ord('^'):
        sservo=14
    elif char == ord('&'):
        sservo=15
    elif char == ord('*'):
        sservo=16

# Zero servos (90 degrees)
    elif char == ord('z'):
        s1=90
        s2=90
        s3=90
        s4=90
        s5=90
        s6=90
        s7=90
        s8=90
        s9=90
        s10=90
        s11=90
        s12=90
        s13=90
        s14=90
        s15=90
        s16=90


    elif char == ord('-'):
        if (sservo==1):
           if (s1>20): s1=s1-2  
        if (sservo==2):
           if (s2>20): s2=s2-2  
        if (sservo==3):
           if (s3>20): s3=s3-2  
        if (sservo==4):
           if (s4>20): s4=s4-2
        if (sservo==5):
           if (s5>20): s5=s5-2  
        if (sservo==6):
           if (s6>20): s6=s6-2  
        if (sservo==7):
           if (s7>20): s7=s7-2  
        if (sservo==8):
           if (s8>20): s8=s8-2
        if (sservo==9):
           if (s9>20): s9=s9-2  
        if (sservo==10):
           if (s10>20): s10=s10-2  
        if (sservo==11):
           if (s11>20): s11=s11-2  
        if (sservo==12):
           if (s12>20): s12=s12-2
        if (sservo==13):
           if (s13>20): s13=s13-2  
        if (sservo==14):
           if (s14>20): s14=s14-2  
        if (sservo==15):
           if (s15>20): s15=s15-2  
        if (sservo==16):
           if (s16>20): s16=s16-2
           
    elif char == ord('='):
       # if (sservo<160): sservo=sservo+2
        if (sservo==1):
           if (s1<160): s1=s1+2  
        if (sservo==2):
           if (s2<160): s2=s2+2  
        if (sservo==3):
           if (s3<160): s3=s3+2  
        if (sservo==4):
           if (s4<160): s4=s4+2
        if (sservo==5):
           if (s5<160): s5=s5+2  
        if (sservo==6):
           if (s6<160): s6=s6+2  
        if (sservo==7):
           if (s7<160): s7=s7+2  
        if (sservo==8):
           if (s8<160): s8=s8+2
        if (sservo==9):
           if (s9<160): s9=s9+2  
        if (sservo==10):
           if (s10<160): s10=s10+2  
        if (sservo==11):
           if (s11<160): s11=s11+2  
        if (sservo==12):
           if (s12<160): s12=s12+2
        if (sservo==13):
           if (s13<160): s13=s13+2  
        if (sservo==14):
           if (s14<160): s14=s14+2  
        if (sservo==15):
           if (s15<160): s15=s15+2  
        if (sservo==16):
           if (s16<160): s16=s16+2  
                
    print sservo
    # Send info to servos
    myservo[0].write(s1)
    myservo[1].write(s2)
    myservo[2].write(s3)
    myservo[3].write(s4)
    myservo[4].write(s5)
    myservo[5].write(s6)
    myservo[6].write(s7)
    myservo[7].write(s8)
    myservo[8].write(s9)
    myservo[9].write(s10)
    myservo[10].write(s11)
    myservo[11].write(s12)
    myservo[12].write(s13)
    myservo[13].write(s14)
    myservo[14].write(s15)
    myservo[15].write(s16)

  
    time.sleep(0.1)

# Close down properly
curses.nocbreak()
key.keypad(0)
curses.echo()
curses.endwin()
# GPIO.cleanup()
