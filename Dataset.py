
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
        for line in range(1, len(lines)):
            self.rides.append(Ride(lines[line], line - 1))


def print_car_rides(rides):
    str = ""
    for ride in rides:
        str += ride.id + ", "
    print("this vehicle is assigned ", len(ride), ("rides : [" if len(rides) > 1 else "ride : ["), str[:2], "]")

ds = Dataset()

if __name__ == "__main__":
    for cycle in range(0, ds.nb_steps):
        for car in ds.cars:
            if car.in_ride:

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
                if car.pos.x == car.current_ride.end.x and car.pos.y == car.current_ride.end.y:
                    car.in_ride = False
                    car.current_ride = get_a_ride(car, cycle)
    for car in ds.cars:
        print_car_rides(car.rides)
