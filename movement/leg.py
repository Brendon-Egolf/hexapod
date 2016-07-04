#!/usr/bin/python

from __future__ import print_function
from __future__ import division
from servo import Servo
import time
import json
import math

class Leg:
    def __init__(self, name):
        self.leg_data = self.get_leg_data()
        self.name = name
        self.servos = {
            "coaxa": self.get_servo('coaxa'),
            "femur": self.get_servo('femur'),
            "tibia": self.get_servo('tibia')
        }
        self.limits = self.leg_data['limits']
#        self.set_leg(self.leg_data['boot_point'])

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
    
    def get_alpha_angle(self, displacement):
        """alpha is th angle between displacement and femur length it is not he angle to write to the femur servo"""
        femur_length = self.get_length('femur')
        tibia_length = self.get_length('tibia')
        numerator = ((femur_length**2) + (displacement**2)) - (tibia_length**2)
        denominator = 2 * femur_length * displacement
        quotient = numerator / denominator
        radians = math.acos(quotient)
        degrees = math.degrees(radians)
        return degrees

    def get_beta_angle(self, displacement):
        """beta is the angle between femur length and tibia length it is not the angle to write to the tibia servo"""
        femur_length = self.get_length('femur')
        tibia_length = self.get_length('tibia')
        numerator = ((femur_length**2) + (tibia_length**2)) - (displacement**2)
        denominator = 2 * femur_length * tibia_length
        quotient = numerator / denominator
        radians = math.acos(quotient)
        degrees = math.degrees(radians)
        print(degrees)
        return degrees

    def set_leg(self, coordinate):
        radius = coordinate['radius']
        displacement = self.get_displacement(coordinate['radius'], coordinate['phi'])
        coaxa_angle = coordinate['theta']
        femur_angle = self.get_femur_angle(radius, displacement)
        tibia_angle = self.get_tibia_angle(displacement)
        self.set_servo('coaxa', coaxa_angle)
        self.set_servo('femur', femur_angle)
        self.set_servo('tibia', tibia_angle)
        print(displacement)
        print(femur_angle, tibia_angle)

    def get_displacement(self, radius, phi):
        coaxa_length = self.get_length('coaxa')
        displacement = math.sqrt((coaxa_length**2)+(radius**2)-(2*coaxa_length*radius
                        *math.cos(math.radians(phi))))
        return displacement

    def get_femur_reference_angle(self, radius, displacement):
        """femur reference angle is the angle between coaxa length and displacement"""
        coaxa_length = self.get_length('coaxa')
        numerator = ((coaxa_length**2) + (displacement**2)) - (radius**2)
        denominator = 2 * coaxa_length * displacement
        quotient = numerator / denominator
        radians = math.acos(quotient)
        degrees = math.degrees(radians)
        return degrees

    def get_working_angle(self, intialAngle, offsetAngle):
        """compresses the servo offset into the working angle which is either alpha or beta"""
        return intialAngle + offsetAngle

    def get_femur_angle(self, radius, displacement):
        alpha_angle = self.get_alpha_angle(displacement)
        print('alpha', alpha_angle)
        femur_offset = self.get_offset('femur')
        reference_angle = self.get_femur_reference_angle(radius, displacement)
        print('reference', reference_angle)
        working_angle = self.get_working_angle(alpha_angle, femur_offset)
        return working_angle - (180 - reference_angle)

    def get_tibia_angle(self, displacement):
        beta_angle = self.get_beta_angle(displacement)
        tibia_offset = self.get_offset('tibia')
        working_angle = self.get_working_angle(beta_angle, tibia_offset)
        return working_angle - 135

    def get_offset(self, leg):
        return self.leg_data['dimensions']['offsets'][leg]

    def get_length(self, leg):
        return self.leg_data['dimensions']['lengths'][leg]
