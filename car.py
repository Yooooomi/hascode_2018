#!/bin/python3

from vec import *

class Car:
    def __init__(self):
        self.pos = Vec(0, 0)
        self.in_ride = False
        self.active = True
        self.current_ride = 0
        self.rides = []

    def get_distance(self, ride):
        return calc_dist(ride.start, self.pos)

    def get_to(self, ride):
        if self.in_ride:
            to_end = calc_dist(self.pos, self.current_ride.end)
            end_to_start = calc_dist(self.current_ride.end, ride.start)
            return to_end + end_to_start
        else:
            return self.get_distance(ride)

    def compute_time_to_this_ride(self, ride):
        return self.get_to(ride)