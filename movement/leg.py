#!/usr/bin/python

from servo import Servo
import time
import json
import numpy

class Leg:
    def __init__(self, name, limits):
        self.leg_data = self.get_leg_data()
        self.name = name
        self.servos = {
            "coaxa": self.get_servo('coaxa'),
            "femur": self.get_servo('femur'),
            "tibia": self.get_servo('tibia')
        }
        self.limits = limits
        print self.get_tibia_angle(self.leg_data['boot_point']['radius'])

    def get_leg_data(self):
        with open('leg-data.json') as json_file:
            return json.load(json_file)

    def get_servo(self, servo_name):
        return Servo(
                self.leg_data[self.name][servo_name],
                servo_name,
                self.leg_data[self.name]['breakout'])

    def set_servo(self, name, angle):
        if angle > self.limits[name]['maximum']:
            angle = self.limits[name]['maximum']
        if angle < self.limits[name]['minimum']:
            angle = self.limits[name]['minimum']
        self[name].set_position(angle)

    def set_limits(self, limits):
        self.limits = limits
    
    def get_femur_angle(self):
        return 1

    def get_tibia_angle(self, radius):
        dimensions = self.leg_data['dimensions']
        return numpy.arccos(((numpy.square(dimensions['femur']) +
                    numpy.square(dimensions['tibia'])) -
                    numpy.square(radius)) /
                    (2 * dimensions['femur'] * dimensions['tibia']))

