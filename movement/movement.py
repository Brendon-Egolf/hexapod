#!/usr/bin/python

from .leg import Leg
from .path import Path
import json


class Movement:
    def __init__(self, velocity_data):
        """
        :param velocity_data: {x-transform, y-transform, z-transform, x-rotate, y-rotate, z-rotate}, each valued -1 to 1
        :type velocity_data: dict
        """
        self.body_data = self.get_body_hard_data()
        self.displacement_data = {
            "x-rot": 0,
            "y-rot": 0,
            "height": 10,
            "leg_distance": 10
        }  # contains values non-auto resetting
        self.velocity_data = velocity_data
        self.paths = []
        self.legs = []
        for i in range(1, 7):
            leg_name = 'leg_' + str(i)
            self.legs[i] = self.get_leg(leg_name)
        self.set_paths()

    def set_velocity_data(self, velocity_data):
        """
        :param velocity_data: the new velocity data passed from main
        """
        self.velocity_data = velocity_data

    def set_paths(self):
        for i in range(1, 7):
            leg_index = i
            self.paths[i] = self.get_path(leg_index, self.velocity_data, self.displacement_data)

    def set_leg(self, leg):
        print(self)

    def get_path(self, leg_index, velocity_data, displacement_data):
        return Path(leg_index, velocity_data, displacement_data, self.body_data)

    def get_gait(self):
        print(self)

    def get_pickup(self):
        print(self)

    def get_calibrate_leg_direction(self):
        print(self)

    def get_leg(self, leg_name):
        print(self)
        return Leg(leg_name)

    @staticmethod
    def get_body_hard_data():
        with open('body-data.json') as json_file:
            return json.load(json_file)
