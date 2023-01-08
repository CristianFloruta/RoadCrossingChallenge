from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []

    def create_car(self):
        chance_to_create_car = randint(1, 6)
        if chance_to_create_car == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(choice(COLORS))
            new_car.penup()
            y_coord = randint(-250, 250)
            new_car.goto(280, y_coord)
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            x_coord = car.xcor() - MOVE_INCREMENT
            y_coord = car.ycor()
            car.goto(x_coord, y_coord)
