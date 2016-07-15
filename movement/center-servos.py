#!/usr/bin/python

from .servo import Servo

coaxa = Servo(0, 'coaxa', 0)
femur = Servo(1, 'femur', 0)
tibia = Servo(2, 'tibia', 0)

coaxa.set_position(0)
femur.set_position(0)
tibia.set_position(0)
