#!/usr/bin/python

import Adafruit_PCA9685
import time
import json
from pprint import pprint


class Servo:
    def __init__(self, port, name, breakout):
        servo_data = self.get_servo_data()
        self.init_pwm(breakout, servo_data['frequency'])
        self.port = port
        self.center = servo_data[name]['center']
        self.boot = servo_data[name]['boot']
        self.minimum = servo_data[name]['minimum']
        self.maximum = servo_data[name]['maximum']
        self.step = servo_data['step']
        self.travel = servo_data['travel']
        self.write_pwm(self.boot)

    def init_pwm(self, breakout, frequency):
        BREAKOUT_ZERO_ADDRESS = 0x40
        BREAKOUT_ONE_ADDRESS = 0x41
        if breakout == 0:
            self.pwm = Adafruit_PCA9685.PCA9685(address=BREAKOUT_ZERO_ADDRESS, busnum=2);
        elif breakout == 1:
            self.pwm = Adafruit_PCA9685.PCA9685(address=BREAKOUT_ONE_ADDRESS, busnum=2);
            
        self.pwm.set_pwm_freq(frequency)
        
    def get_servo_data(self):
        with open('servo-data.json') as json_file:
            return json.load(json_file)
    
    def angle_pwm(self, angle):
        pwm = self.center + (angle * (self.travel / self.step))
        if pwm >= self.maximum:
            pwm = self.maximum
            print 'Maximum Limit'
        if pwm <= self.minimum:
            pwm = self.minimum
            print 'Minimum Limit'
        return pwm 

    def write_pwm(self, pwm):
        self.pwm.set_pwm(self.port, 0, pwm)

    def set_position(self, angle):
        pwm = self.angle_pwm(angle)
        self.write_pwm(pwm)

