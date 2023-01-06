from turtle import Turtle
from random import choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.color(choice(COLORS))
        self.penup()

        self.goto(280, STARTING_MOVE_DISTANCE)

    def move_forward(self):
        x_coord = self.xcor() - MOVE_INCREMENT
        y_coord = self.ycor()
        self.goto(x_coord, y_coord)

    def new_car(self):
        pass

