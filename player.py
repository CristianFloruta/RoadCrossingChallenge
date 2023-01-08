from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
PLAYER_COLOR = "navy blue"


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color(PLAYER_COLOR)
        self.penup()
        self.setheading(90)
        self.goto_start()

    def move(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(0, new_y)

    def goto_start(self):
        self.goto(STARTING_POSITION)
