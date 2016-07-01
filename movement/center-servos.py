#!/usr/bin/python

from servo import Servo
import time

while True:
    for i in range(14,11):
        print 'instantiating servo: ', i
        servo = Servo(i, 'coaxa', 0)
        servo.set_position(0)
        time.sleep(.5)
