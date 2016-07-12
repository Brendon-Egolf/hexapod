#!/usr/bin/python

# noinspection PyUnresolvedReferences
import Adafruit_PCA9685
import time
import json
from pprint import pprint


class Servo:
    def __init__(self, port, name, breakout):
        servo_data = self.get_servo_data()
        self.pwm = self.get_pwm(breakout, servo_data['frequency'])
        self.port = port
        self.center = servo_data[name]['center']
        self.boot = servo_data[name]['boot']
        self.minimum = servo_data[name]['minimum']
        self.maximum = servo_data[name]['maximum']
        self.step = servo_data['step']
        self.travel = servo_data['travel']
#       self.write_pwm(self.boot)

    @staticmethod
    def get_pwm(breakout, frequency):
        breakout_addresses = [0x40, 0x41]
        pwm = Adafruit_PCA9685.PCA9685(
                address=breakout_addresses[breakout],
                busnum=2)
        pwm.set_pwm_freq(frequency)
        return pwm
        
    @staticmethod
    def get_servo_data():
        with open('servo-data.json') as json_file:
            return json.load(json_file)
    
    def angle_pwm(self, angle):
        pwm = self.center + (angle * (self.travel / self.step))
        if pwm >= self.maximum:
            pwm = self.maximum
            print('Maximum Limit')
        if pwm <= self.minimum:
            pwm = self.minimum
            print('Minimum Limit')
        return int(pwm)

    def write_pwm(self, pwm):
        self.pwm.set_pwm(self.port, 0, pwm)

    def set_position(self, angle):
        pwm = self.angle_pwm(angle)
        self.write_pwm(pwm)

