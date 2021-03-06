from car import *
from vec import *
import sys
from Ride import *

class Dataset:

    def __init__(self, path):
        self.nb_cars = 0
        self.nb_steps = 0
        self.cars = []
        self.rides = []
        file = open(path)
        lines = file.readlines()
        first_line = lines[0].split()
        self.nb_cars = int(first_line[2])
        self.nb_steps = int(first_line[5])
        for i in range(0, self.nb_cars):
            self.cars.append(Car())
        for line in range(1, len(lines)):
            self.rides.append(Ride(lines[line], line - 1))

    def get_a_ride(self, car, cycle):
        list_ride = []
        for ride in self.rides:
            if ride.available and ride.is_possible(cycle + car.get_to(ride)):
                list_ride.append(ride)
        if len(list_ride) == 0:
            car.active = False
            return 0
        best_ride = list_ride[0]
        wait = best_ride.earliest - cycle - car.get_distance(best_ride)
        if (wait < 0):
            wait = 0
        time = car.get_distance(best_ride) + wait
        best_time = time
        for ride in list_ride:
            wait = ride.earliest - cycle - car.get_distance(ride)
            if (wait < 0):
                wait = 0
            time = car.get_distance(ride) + wait
            if time < best_time:
                best_ride = ride
                best_time = time
        return best_ride


def print_car_rides(rides):
    string = ""
    for ride in rides:
        string += str(ride.id)
        string += " "
    print(len(rides), string[:-1])


if __name__ == "__main__":
    ds = Dataset(sys.argv[1])
    for cycle in range(0, ds.nb_steps):
        for car in ds.cars:
            if car.in_ride and cycle >= car.current_ride.earliest:
                x = car.pos.x - car.current_ride.end.x
                y = car.pos.y - car.current_ride.end.y
                if x != 0:
                    if x > 0:
                        car.pos.x -= 1
                    else:
                        car.pos.x += 1
                else:
                    if y > 0:
                        car.pos.y -= 1
                    else:
                        car.pos.y += 1
            if car.active and ((not car.in_ride) or (car.pos.x == car.current_ride.end.x and car.pos.y == car.current_ride.end.y)):
                car.in_ride = False
                ride = ds.get_a_ride(car, cycle)
                if ride != 0:
                    ride.available = False
                    car.current_ride = ride
                    car.in_ride = True
                    car.rides.append(ride)
    for car in ds.cars:
        print_car_rides(car.rides)