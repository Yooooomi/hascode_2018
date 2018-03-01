
class Dataset:

    def __init__(self, path):
        self.nb_cars = 0
        self.cars = []
        self.rides = []
        self.nb_steps = 0
        file = open(path)
        lines = file.readlines()
        first_line = lines[0].split()
        self.nb_cars = int(first_line[2])
        self.nb_steps = int(first_line[5])
        for line in range(1, len(lines)):
            self.rides.append(Ride(lines[line]))