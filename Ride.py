from vec import Vec


class Ride:
	def __init__(self, line):
		array = line.split(' ')
		self.start = Vec(int(array[0]), int(array[1]))
		self.end = Vec(int(array[2]), int(array[3]))
		self.earliest = int(array[4])
		self.latest = int(array[5])
		self.available = True
