#!/bin/python3

from vec import *

class car:
    def __init__(self):
        self.pos = Vec(0, 0)
        self.in_ride = False
        self.active = True
        self.current_ride = 0
        self.rides = []

    def get_distance(self, ride):
        return calc_dist(ride.start, self.pos)