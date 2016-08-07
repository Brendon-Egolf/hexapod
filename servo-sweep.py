#!/usr/bin/python

from movement.servo import Servo
import time

servo = Servo(0, 'coaxa', 0)
MIN = -60
MAX = 60
while True:
    servo.set_position(MIN)
    time.sleep(.5)
    servo.set_position(MAX)
