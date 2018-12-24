# Robot with IR sensors
# Turns when sensors encounter line
# r and l now turn the servo for camera

import RPi.GPIO as GPIO
import time
import curses
# Pin Assignments
servo_pin = 12
duty_cycle = 7.5

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(16, GPIO.IN)
GPIO.setup(18, GPIO.IN)
GPIO.setup(22, GPIO.IN)

GPIO.setup(servo_pin, GPIO.OUT)
pwm_servo = GPIO.PWM(servo_pin, 50)
pwm_servo.start(duty_cycle)

key=curses.initscr()
#curses.cbreak()
key.keypad(1)
key.nodelay(1)

def Forward():
    GPIO.output(7, False)
    GPIO.output(11, True)
    GPIO.output(13, False)
    GPIO.output(15, True)

def Back():
    GPIO.output(7, True)
    GPIO.output(11, False)
    GPIO.output(13, True)
    GPIO.output(15, False)

def Right():
    GPIO.output(7, True)
    GPIO.output(11, False)
    GPIO.output(13, False)
    GPIO.output(15, True)

def Left():
    GPIO.output(7, False)
    GPIO.output(11, True)
    GPIO.output(13, True)
    GPIO.output(15, False)

def Stop():
    GPIO.output(7, False)
    GPIO.output(11, False)
    GPIO.output(13, False)
    GPIO.output(15, False)

try:
    while (True):
        char=key.getch()
        if char==ord('q'):
            break
        elif char==ord('b'):
            Back()
            time.sleep(.1)
            Stop() 
        elif char==ord('f'):
            pwm_servo.ChangeDutyCycle(7.5)
        elif char==ord('r'):
            pwm_servo.ChangeDutyCycle(4)    
        elif char==ord('l'):
            pwm_servo.ChangeDutyCycle(11)
        elif char==ord('s'):
            Stop()
            time.sleep(1)
        if GPIO.input(22)==1 and GPIO.input(16)==1:
            Stop()
            time.sleep(1)
        elif GPIO.input(22)==1 and GPIO.input(16)==0:
            Right()
            time.sleep(.1)
        elif GPIO.input(16)==1 and GPIO.input(22)==0:
            Left()
            time.sleep(.1)
        else:
            Forward()
            time.sleep(.1)
finally:
    pwm_servo.ChangeDutyCycle(7.5)
    Stop()
#    curses.nocbreak()
    key.keypad(0)
    curses.echo()
    curses.endwin()
    GPIO.cleanup()
