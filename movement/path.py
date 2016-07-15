#!/usr/bin/python


class Path:
    def __init__(self, leg_index, velocity_data, displacement_data, body_data):
        self.leg_index = leg_index
        self.velocity_data = velocity_data
        self.displacement_data = displacement_data
        self.body_data = body_data
        self.equation = self.get_equation()

    def get_point(self, frame):
        """
        :param frame: equivalent to the parametric variable t
        :return:
        """
        print(self)

    def get_equation(self, equation_name):
        print(self)
        return '2 + 2'

    def get_origin(self):
        print(self)

    def get_range(self):
        print(self)
