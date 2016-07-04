#!/usr/bin/python

from servo import Servo

coaxa = Servo(4, 'coaxa', 1)
femur = Servo(5, 'femur', 1)
tibia = Servo(6, 'tibia', 1)

coaxa.set_position(0)
femur.set_position(0)
tibia.set_position(0)
