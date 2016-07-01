#!/usr/bin/python

from __future__ import division
from servo import Servo
import time
import json
import math

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
        self.set_leg(self.leg_data['boot_point'])

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
        self.servos[name].set_position(angle)

    def set_limits(self, limits):
        self.limits = limits
    
    def get_femur_angle(self, displacement, phi):
        """uses the inverse law of cosines to find femur angle from displacement"""
        lengths = self.leg_data['dimensions']['lengths']
#direction = phi ? : phi / abs(phi)
        return (phi + math.degrees(math.acos((
                              ((lengths['femur']**2)
                            + (displacement**2))
                            - (lengths['tibia']**2))
                            /
                              (2 * (lengths['femur']) * (displacement)))))

    def get_tibia_angle(self, displacement):
        """uses the inverse law of cosines to find tibia angle from displacement"""
        lengths = self.leg_data['dimensions']['lengths']
        return (180 + math.degrees(math.acos((
                              ((lengths['femur']**2)
                            + (lengths['tibia']**2))
                            - (displacement**2))
                            /
                              (2 * (lengths['femur']) * (lengths['tibia'])))))

    def set_leg(self, coordinate):
        self.set_servo('coaxa', coordinate['theta'])
        self.set_servo('femur', self.get_femur_angle(self.get_displacement(coordinate['radius'], coordinate['phi']), coordinate['phi']))
        self.set_servo('tibia', self.get_tibia_angle(self.get_displacement(coordinate['radius'], coordinate['phi'])))

    def get_displacement(self, radius, phi):
        coaxaLength = self.leg_data['dimensions']['lengths']['coaxa']
        return (math.sqrt((coaxaLength**2)+(radius**2)-(2*coaxaLength*radius
                        *math.cos(phi))))


