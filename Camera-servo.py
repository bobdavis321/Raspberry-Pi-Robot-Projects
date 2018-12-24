# Camera Servo Keyboard control
# 
# u=up, d=down
# r=right, l=left
# q=quit

# import curses and GPIO
import curses
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)

# GPIO numbering & define output pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
p7=GPIO.PWM(7,50)
p11=GPIO.PWM(11,50)
p7.start(5)
p11.start(5)

# Turn on instant key response
key = curses.initscr()
curses.cbreak()
key.keypad(1)
key.nodelay(1)
pos7=10
pos11=10

while True:   
    char = key.getch()
    if char == ord('q'):
        break
    elif char == ord('r'):
        if (pos7<12):
            pos7=pos7+1
    elif char == ord('l'):
        if (pos7>1):
            pos7=pos7-1
    elif char == ord('u'):
        if (pos11<12):
            pos11=pos11+1
    elif char == ord('d'):
        if (pos11>1):
            pos11=pos11-1
    p7.ChangeDutyCycle(pos7)    
    p11.ChangeDutyCycle(pos11)    
    time.sleep(1)
 
# Close down properly
p7.stop
p11.stop
curses.nocbreak()
key.keypad(0)
curses.echo()
curses.endwin()
GPIO.cleanup()
    
