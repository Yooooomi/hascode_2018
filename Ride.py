from vec import *


class Ride:
	def __init__(self, line, ride_id):
		array = line.split(' ')
		self.start = Vec(int(array[0]), int(array[1]))
		self.end = Vec(int(array[2]), int(array[3]))
		self.earliest = int(array[4])
		self.latest = int(array[5])
		self.available = True
		self.id = ride_id

	def is_possible(self, cycle):
		dist = calc_dist(self.start, self.end)
		if dist + cycle < self.latest:
			return True
		else:
			return False

