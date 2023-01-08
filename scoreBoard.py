from turtle import Turtle

FONT = ("Courier", 18, "bold")



class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 1
        self.penup()
        self.hideturtle()
        self.goto(-260, 260)
        self.write(f"Level {self.score}", align="left", font=FONT)

    def level_up(self):
        self.score += 1
        self.clear()
        self.write(f"Level {self.score}", align="left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)