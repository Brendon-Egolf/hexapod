#!/usr/bin/python

from servo import Servo
import time


def set_servos(position):
    for i in range(4,7):
        print 'instantiating servo: ', i
        servo = Servo(i, 'coaxa', 1)
        servo.set_position(position)
        time.sleep(.5)


for i in range(61):
    set_servos(i)
    time.sleep((i*.00266666666) + .001)
    set_servos(-i)
