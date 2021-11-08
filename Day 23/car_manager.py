from car import Car
import random


def generate_unique_y(used_y):
    unique_y_found = False
    y = 0
    while not unique_y_found:
        y = random.randint(-12, 13 )
        if y not in used_y:
            used_y.append(y)
            unique_y_found = True
    return y


class CarManager:
    def __init__(self, player):
        self.cars = []
        self.generate_cars()
        self.time_left_to_generated = 0
        self.target = player

    def generate_cars(self):
        used_y = []
        for _ in range(7):
            y = generate_unique_y(used_y)
            print(y)
            position = (270 + (random.randint(5, 10) * 20), y * 20)
            self.cars.append(Car(starting_position=position, callback=self.destroy_car))

    def update(self):
        self.move_cars()
        if self.time_left_to_generated == 0:
            self.generate_cars()
            self.time_left_to_generated = 20
        else:
            self.time_left_to_generated -= 1

    def collision_check(self):
        is_collided = False
        for car in self.cars:
            if car.is_collided_with_player(self.target):
                is_collided = True
                break
        return is_collided

    def move_cars(self):
        for car in self.cars:
            car.move_forward()

    def destroy_car(self, car):
        self.cars.remove(car)
