#Uses PCA9685 to run 2 hands or 12 servos.
#Moves each servo forward and backwards

import time
from SunFounder_PCA9685 import Servo

myservo = []
for i in range(0,12):
        myservo.append(Servo.Servo(i))  # channel 1
        Servo.Servo(i).setup()

while True:
    for c in range(0,12):
        for i in range(50, 130, 10):
                print i
                myservo[c].write(i)
                time.sleep(0.1)
        for i in range(130, 50, -10):
                print i
                myservo[c].write(i)
                time.sleep(0.1)
        myservo[c].write(90)
