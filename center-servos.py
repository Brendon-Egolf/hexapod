#!/usr/bin/python

from movement.servo import Servo

for i in range(0, 4):
    base_port = i * 4
    coaxa = Servo(i, 'coaxa', 0)
    femur = Servo(i + 1, 'femur', 0)
    tibia = Servo(i + 2, 'tibia', 0)

    coaxa.set_position(0)
    femur.set_position(0)
    tibia.set_position(0)
