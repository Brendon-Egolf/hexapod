#!/usr/bin/python

from servo import Servo
import time

servo = Servo(0, 'coaxa', 0)
time.sleep(1)
servo.set_position(60)
