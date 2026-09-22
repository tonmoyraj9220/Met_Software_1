class car:

    def __init__(self, reg_number, max_speed):
        self.registration_number = reg_number
        self.maximum_speed = max_speed
        self.current_speed = 0
        self.distance = 0

car1 = car("ABC-123", 142)

print(f"Car {car1.registration_number} has max speed of {car1.maximum_speed} current speed of {car1.current_speed} and distance of {car1.distance}")