import random

class Car:
    def __init__(self, license_plate, maximum_speed):
        self.license_plate = license_plate
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        self.current_speed += speed_change

        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed

        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        distance = self.current_speed * hours
        self.travelled_distance += distance


def race(cars):
    race_finished = False

    while not race_finished:
        for car in cars:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)

            car.drive(1)

            if car.travelled_distance >= 10000:
                race_finished = True
                break

    return cars