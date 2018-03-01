from Vec import Vec


class Ride:
	def __init__(self, line):
		array = line.split(' ')
		self.start = Vec(int(array[0]), int(array[1]))
		self.end = Vec(int(array[2]), int(array[3]))
		self.earliest = Vec(int(array[4]), int(array[5]))
		self.available = True
