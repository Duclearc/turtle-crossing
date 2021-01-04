from turtle import Turtle
from random import randint, choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
SAFE_ZONE = 100


class CarManager:
    def __init__(self, screen_height, screen_width):
        self.all_cars = []
        self.SCREEN_HEIGHT = int(screen_height / 2) - SAFE_ZONE
        self.SCREEN_WIDTH = int(screen_width / 2)
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        """creates a new car and adds it to all_cars list"""
        if randint(1, 6) == 1:
            car = Turtle()
            car.shape('square')
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.color(choice(COLORS))
            random_y = randint(-self.SCREEN_HEIGHT, self.SCREEN_HEIGHT)
            car.goto((self.SCREEN_WIDTH, random_y))
            self.all_cars.append(car)

    def move_cars(self):
        """moves each of the cars according to their speed"""
        for car in self.all_cars:
            car.backward(self.car_speed)

    def increase_cars_speed(self):
        """increases the cars' speed by a pre-determinate increment"""
        self.car_speed += MOVE_INCREMENT
