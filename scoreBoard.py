from turtle import Turtle

FONT = ("Courier", 18, "bold")



class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(-260, 260)
        self.write(f"Level {self.score}", align="left", font=FONT)

    def level_up(self):
        self.score += 1
        self.clear()
        self.write(f"Level {self.score}", align="left", font=FONT)
